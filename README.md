# recommendersystem
Open Source Repository for educational purposes only 
ENTRYPOINT ["python3", "main.py"]

# #####################################################################################
# ############################# How to run each Component #############################
# #####################################################################################

# src\refactoring_scripts\datasetRefactoring.py
- Ziel: Den Datensatz so umstrukturieren, dass er im weiteren Verlauf/bei den Berechnungen zu verwenden ist
- Ausführen: Einfach als Python Skript laufen lassen
- Hinweis: Damit das Ausführen klappt, wird der Rohdatensatz von Netzflix im Workspace benötigt. Dieser ist aufgrund seiner Größe im Gitignore des Projektes. Die Pfade müssten lauten:
    - src\dataset\combined_data_1.txt
    - src\dataset\combined_data_2.txt
    - src\dataset\combined_data_3.txt
    - src\dataset\combined_data_4.txt
- Ausgaben: 
    - Laufzeit als Konsolenausgabe
    - Der umstrukturierte Datensatz als .csv Datei

# src\refactoring_scripts\item-based_calculation.py
- Ziel: Den Datensatz sinnvoll verkleinern und ein Modell berechnen, das zu jeder Filmid die 10 nächsten Nachbarn enthält
- Ausführen: Einfach als Python Skript laufen lassen
- Hinweis: Damit das Ausführen klappt, wird der oben berechnete refactored_data_complete Datensatz im Workspace benötigt. Dieser ist aufgrund seiner Größe im Gitignore des Projektes. Der Pfad müsste lauten:
    - refactored_data_complete.csv
- Ausgaben: 
    - Laufzeiten (Verkleinern "Runtime filter", Modell berechnen "Runtime model" und Gesamt "Runtime script") als Konsolenausgabe
    - Das Modell als .csv Datei mit Indices (neighbours.csv)
    - Das Modell als .csv Datei mit Filmids (neighbours_ids.csv)

# src\evaluation\testset_creation.py
- Ziel: Einen Testdatensatz kreieren 
- Ausführen: Einfach als Python Skript laufen lassen
- Hinweis: Damit das Ausführen klappt, wird der oben berechnete refactored_data_complete Datensatz im Workspace benötigt. Dieser ist aufgrund seiner Größe im Gitignore des Projektes. Der Pfad müsste lauten:
    - refactored_data_complete.csv
- Ausgaben: 
    - Laufzeit als Konsolenausgabe
    - Testdatensatz als .json Datei mit 1000 Dicts der Form: {'User_Id' : 123, 'Prediction_Base' : [1,2,3,4,5], 'Raw_true' : [10,20,75,55,66,90,...]}

# src\evaluation\testset_processing.py
- Ziel: Kennzahlen zur Evaluation berechnen
- Ausführen: Einfach als Python Skript laufen lassen
- Ausgaben: 
    - Laufzeit als Konsolenausgabe
    - Mean Precision als Konsolenausgabe
    - Mean Recall als Konsolenausgabe