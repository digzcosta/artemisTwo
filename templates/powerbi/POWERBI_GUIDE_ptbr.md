### Dashboard (Power BI)

1. Gere os arquivos CSV usando o comando CLI `export-powerbi`
2. Abra o Power BI Desktop
3. Abra o template do dashboard em:
   `templates/powerbi/artemis_powerbi_template.pbit`
4. Quando solicitado, selecione a pasta:
   `exports/powerbi/`
5. Aguarde o carregamento do dashboard
6. Para atualizar os dados após gerar novos CSVs:
   - Vá em Home → Refresh
   - Utilize apenas a opção padrão (Refresh / Data)

⚠️ Não utilize as opções "Schema" ou "Data + Schema".
Essas opções podem gerar avisos de parâmetros e não são necessárias
para o funcionamento do dashboard.