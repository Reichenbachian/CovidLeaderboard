---
title: "{{ replace .Name "-" " " | title }}" # The name of the school
id: "{{ .Name }}" # The id of the school in the JSON blob
opened: {{ .Date }} # When the school's classes started
everyone: true # Whether the school has invited everyone back to campus
---
