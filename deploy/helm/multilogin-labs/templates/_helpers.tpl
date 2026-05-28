{{/* helpers placeholder so chart lints cleanly */}}
{{- define "multilogin-labs.labels" -}}
app.kubernetes.io/name: multilogin-labs
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}
