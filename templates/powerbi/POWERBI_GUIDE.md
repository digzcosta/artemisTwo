Dashboard (Power BI)
	1.	Generate the CSV files using the CLI command export-powerbi
	2.	Open Power BI Desktop
	3.	Open the dashboard template located at:
templates/powerbi/artemis_powerbi_template.pbit
	4.	When prompted, select the folder:
exports/powerbi/
	5.	Wait for the dashboard to load
	6.	To refresh the data after generating new CSV files:
	•	Go to Home → Refresh
	•	Use only the default option (Refresh / Data)

⚠️ Do not use the “Schema” or “Data + Schema” options.
These options may trigger parameter warnings and are not required
for the dashboard to function correctly.