#!/usr/bin/env bash

set -e


### These are the parameters you can set when calling this script:
NAMESPACE="${NAMESPACE:-default}"
###


if [[ ! $(kubectl get serviceaccount --namespace ${NAMESPACE} | grep "github-actions-${NAMESPACE}") ]]
then
    echo "⏳ Creating service account \"github-actions-${NAMESPACE}\" for namespace \"${NAMESPACE}\""
    kubectl create serviceaccount "github-actions-${NAMESPACE}" --namespace ${NAMESPACE}
    kubectl create rolebinding "github-actions-${NAMESPACE}" --clusterrole edit --serviceaccount ${NAMESPACE}:"github-actions-${NAMESPACE}"
    echo "✅ Service account created"
else
    echo "✅ Service account \"github-actions-${NAMESPACE}\" for namespace \"${NAMESPACE}\" already exists"
fi
echo

echo "⏳ Fetching service account credentials..."
SA_SECRET_NAME=$(kubectl get serviceaccount "github-actions-${NAMESPACE}" --namespace "${NAMESPACE}" --output go-template='{{ (index .secrets 0).name }}')
echo "✅ Service account credentials fetched."
echo

echo "⏳ Adding Kubernetes API server to kubectl configuration..."
KUBECONFIG_SERVER=$(kubectl config view --minify --output go-template='{{ (index .clusters 0).cluster.server }}')
kubectl get secret $SA_SECRET_NAME --namespace "${NAMESPACE}" --output go-template='{{ index .data "ca.crt" }}' | base64 --decode > /tmp/kubeconfig-ca.crt
kubectl --kubeconfig /tmp/kubeconfig.yml config set-cluster brassberry --server=$KUBECONFIG_SERVER --certificate-authority /tmp/kubeconfig-ca.crt --embed-certs=true
rm /tmp/kubeconfig-ca.crt
echo "✅ Kubernetes API server added."
echo

echo "⏳ Adding authentication token to kubectl configuration..."
KUBECONFIG_TOKEN=$(kubectl get secret $SA_SECRET_NAME --namespace "${NAMESPACE}" --output go-template='{{ .data.token }}' | base64 --decode)
kubectl --kubeconfig /tmp/kubeconfig.yml config set-credentials "github-actions-${NAMESPACE}" --token $KUBECONFIG_TOKEN
kubectl --kubeconfig /tmp/kubeconfig.yml config set-context "github-actions-${NAMESPACE}-brassberry" --cluster brassberry --user "github-actions-${NAMESPACE}" --namespace "${NAMESPACE}"
kubectl --kubeconfig /tmp/kubeconfig.yml config use-context "github-actions-${NAMESPACE}-brassberry"
echo "✅ Authentication token added."
echo

echo "⏳ Converting configuration to base64..."
KUBECONFIG_B64="$(base64 /tmp/kubeconfig.yml)"
rm /tmp/kubeconfig.yml
echo "✅ Configuration converted."
echo

echo "👌 Configuration file ready!"
echo "👇 Use the following value for your GitHub secret:"
echo
echo "${KUBECONFIG_B64}"
echo
