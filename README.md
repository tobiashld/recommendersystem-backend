# recommendersystem
Open Source Repository for educational purposes only 
ENTRYPOINT ["python3", "main.py"]

# Lokaler Start des Backends

### Voraussetzungen 
- python3.10 (https://www.python.org/) 
### Schritte
1. Das Repo klonen mit: `git clone https://github.com/tobiashld/recommendersystem-backend.git`

innerhalb des geklonten Ordners:

#### Windows:
2. Die Pakete installieren mit: `pip install -r requirements.txt`
3. Die App starten mit: `flask --app main:app run`
#### MacOS:
2. Die Pakete installieren mit: `pip3 install -r requirements.txt`
3. Die App starten mit: `flask --app main:app run`



Die API fährt hoch und ist auf der URL: http://127.0.0.1:5000 verfügbar

# Ausführen der Skripte zur Datenverarbeitung

### Refaktorierung des Datensatzes
- **Pfad zum Skript ohne Datum**: src\refactoring_scripts\datasetRefactoring.py
- **Pfad zum Skript mit Datum**: src\refactoring_scripts\datasetRefactoringWithDate.py
- **Ziel**: Den Datensatz so umstrukturieren, dass er im weiteren Verlauf/bei den Berechnungen zu verwenden ist
- **Ausführen**: Einfach als Python Skript laufen lassen
- **Hinweis**: Damit das Ausführen klappt, wird der Rohdatensatz von Netzflix im Workspace benötigt. Dieser ist aufgrund seiner Größe im Gitignore des Projektes. Die Pfade müssten lauten:
    - src\dataset\combined_data_1.txt
    - src\dataset\combined_data_2.txt
    - src\dataset\combined_data_3.txt
    - src\dataset\combined_data_4.txt
- **Ausgaben**: 
    - Laufzeit als Konsolenausgabe
    - Der umstrukturierte Datensatz als .csv Datei ohne Datum (refactored_data_complete.csv)/mit Datum (refactored_data_with_date_complete.csv)

### Explorative Datenanalyse
- **Pfad zum Skript**: src\explorative_analysis\dataanalysis.py
- **Ziel**: Einen Blick auf deskriptive Statistiken des Datensatzes erhalten.
- **Ausführen**: Einfach als Python Skript laufen lassen
- **Hinweis**: Damit das Ausführen klappt, werden die oben berechneten refactored_data_complete und refactored_data_with_date_complete Datensätze im Workspace benötigt. Diese sind aufgrund ihrer Größe im Gitignore des Projektes. Außerdem wird die movie_titles.csv von Netflix benötigt. Das im Schritt "Modellberechnung" erstellte Trainingset wird für den letzten Schritt der Datenanalyse ebenfalls benötigt. Die Pfade müssten lauten:
    - refactored_data_complete.csv
    - refactored_data_with_date_complete.csv
    - trainingset.csv
    - src\dataset\movie_titles.csv
- **Ausgaben**: 
    - Diverse Datenplots als temp.html

### Modellberechnung
- **Pfad zum Skript**: src\refactoring_scripts\item-based_calculation.py
- **Ziel**: Den Datensatz sinnvoll verkleinern und ein Modell berechnen, das zu jeder Filmid die 10 nächsten Nachbarn enthält
- **Ausführen**: Einfach als Python Skript laufen lassen
- **Hinweis**: Damit das Ausführen klappt, wird der oben berechnete refactored_data_complete Datensatz im Workspace benötigt. Dieser ist aufgrund seiner Größe im Gitignore des Projektes. Der Pfad müsste lauten:
    - refactored_data_complete.csv
- **Ausgaben**: 
    - Laufzeiten (Verkleinern "Runtime filter", Modell berechnen "Runtime model" und Gesamt "Runtime script") als Konsolenausgabe
    - Das Modell als .csv Datei mit Indices (neighbours.csv)
    - Das Modell als .csv Datei mit Filmids (neighbours_ids.csv)
    - Das verwendete Trainingsset als .csv Datei (trainingset.csv)

### Erstellung von Testdaten 
- **Pfad zum Skript**: src\evaluation\testset_creation.py
- **Ziel**: Einen Testdatensatz kreieren 
- **Ausführen**: Einfach als Python Skript laufen lassen
- **Hinweis**: Damit das Ausführen klappt, wird der oben berechnete refactored_data_complete Datensatz im Workspace benötigt. Dieser ist aufgrund seiner Größe im Gitignore des Projektes. Der Pfad müsste lauten:
    - refactored_data_complete.csv
- **Ausgaben**: 
    - Laufzeit als Konsolenausgabe
    - Testdatensatz als .json Datei mit 1000 Dicts der Form: {'User_Id' : 123, 'Prediction_Base' : [1,2,3,4,5], 'Raw_true' : [10,20,75,55,66,90,...]}

### Berechnung von Evaluationskennzahlen - Variante A  
- **Pfad zum Skript**: src\evaluation\testset_processing.py
- **Ziel**: Kennzahlen zur Evaluation berechnen bei Rückgabe aller 10 berechneten Nachbarn für jeden Film
- **Ausführen**: Einfach als Python Skript laufen lassen
- **Ausgaben**: 
    - Laufzeit als Konsolenausgabe
    - Mean Precision als Konsolenausgabe
    - Mean Recall als Konsolenausgabe

### Berechnung von Evaluationskennzahlen - Variante B  
- **Pfad zum Skript**: src\evaluation\one_list_evaluation.py
- **Ziel**: Kennzahlen zur Evaluation berechnen bei Rückgabe einer geteilten Empfehlungsliste für den gesamten Input an Filmen
- **Ausführen**: Einfach als Python Skript laufen lassen
- **Ausgaben**: 
    - Laufzeit als Konsolenausgabe
    - Mean Precision als Konsolenausgabe
    - Mean Recall als Konsolenausgabe
