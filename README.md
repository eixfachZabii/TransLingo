# Candidate Select Hackathon mit Deloitte.

Am 25. Oktober 2024 stellte unser **dreiköpfiges Team** beim **Candidate Select Hackathon** 
in München erfolgreich unsere **cloudbasierte KI-Lösung _TransLingo_** vor und konnte
**Deloitte.** überzeugen. _TransLingo_ bietet eine **leistungsstarke** 
und **sichere** Lösung zur **Dokumentenübersetzung** und
**Text-to-Speech-Verarbeitung** speziell für **Behörden** 
und basiert auf einem **Hybrid-Cloud-Ansatz**, der **AWS Translate**
und **AWS Polly** integriert. Die Anwendung erfüllt höchste Ansprüche
an **Skalierbarkeit** und **Kosteneffizienz**, was bei den Vertreter:innen 
von Deloitte auf ausgesprochen positives Feedback stieß.

# TransLingo - Effiziente Dokumentenübersetzung mit Text-to-Speech für Behörden

![Folie 1](doc/images/Folie1.png)

**TransLingo** bietet eine sichere und effiziente Lösung zur Übersetzung und Sprachsynthese von Dokumenten für deutsche Behörden. Die Anwendung verbindet eine hybride Cloud-Architektur zur Wahrung der Datensicherheit und Flexibilität.

---

## Projektübersicht

### Ausgangssituation

![Folie 2](doc/images/Folie2.png)

Eine deutsche Behörde setzt derzeit auf veraltete On-Premise-Systeme, die kostenintensiv und wartungsaufwendig sind. Um die Effizienz zu steigern, wird eine Cloud-basierte Lösung für Dokumentenübersetzung und Text-to-Speech benötigt. Ziel ist die Entwicklung eines **Proof of Concept (PoC)** unter Verwendung von **AWS Translate** und **AWS Polly**.

---

## Anforderungen und Implementierung

### Projektanforderungen
1. **Effizienz**: Skalierbare Cloud-Lösungen für TTS und Übersetzung.
2. **Sicherheit**: TLS/SSL für sichere Datenübertragung, VPN für Onsite-Cloud-Kommunikation.
3. **Kosten**: Reduzierte On-Premise-Kosten durch gezielte Nutzung von Cloud-Ressourcen.
4. **Datenmanagement**: Onsite-Speicherung persönlicher Daten, effiziente Nutzung von AWS-Services für Anfragen ohne sensitive Daten.

### Industriestandards und Technische Details
- **Datenübertragung**: TLS/SSL, gRPC und Protocol Buffers für optimierten und sicheren Datenaustausch.
- **Serverless-Architektur**: Einsatz von AWS Lambda und AWS S3 zur dynamischen Skalierung und einfachen Integration von TTS- und Übersetzungsprozessen.
- **Weitere AWS-Services**: Nutzung von CloudWatch zur Überwachung und Protokollierung der Prozesse.

![Folie 3](doc/images/Folie3.png)

### Lösungsvorschlag: Hybrid-Cloud-Ansatz
- **Cloud-Szenario**: Persönliche Daten werden Onsite gespeichert; rechenintensive Prozesse wie Text-to-Speech laufen in der AWS-Cloud.
- **Sicherheit**: Verschlüsselte Übertragung und Speicherung sensibler Daten, Verwendung von Industriestandards (z. B. TLS/SSL).
- **Skalierbarkeit**: Nutzung von AWS-Services für dynamische Skalierung bei erhöhten Anfragen.
- **Kostenoptimierung**: Pay-per-Use-Modell und flexible Ressourcennutzung in der Cloud.

![Folie 4](doc/images/Folie4.png)

---

## Projektaufbau und Proof of Concept (PoC)

![Folie 5](doc/images/Folie5.png)

### Schritte zur Implementierung
1. **AWS-Anmeldung**: Zugang zum vorkonfigurierten AWS-Konto mit benötigten Berechtigungen.
2. **Infrastrukturaufbau**: Erstellen der benötigten Infrastruktur über AWS-Konsole oder Infrastructure as Code (IaC).
3. **Implementierung der Applikationslogik**: Nutzung von AWS SDK oder API zur Integration von AWS Translate und Polly.
4. **Test und Validierung**: Manuelles Hoch- und Herunterladen von Dateien zur Funktionsprüfung.

### Demo-Funktionen
- **Login Page**: Authentifizierter Zugang zur Anwendung.
- **Upload Page**: Sicherer Upload und Verarbeitung von Dokumenten.
- **TransLingu Prototype**: Prototyp des TransLingo Text-to-Speech tools

![Folie 6](doc/images/Folie6.png)
![Folie 7](doc/images/Folie7.png)
![Folie 8](doc/images/Folie8.png)

---

## Feedback und Verbesserung

Wir freuen uns über Feedback zur Nutzung und Performance der Lösung. Für Fragen oder Anmerkungen kontaktieren Sie uns gerne!

![Folie 9](doc/images/Folie9.png)

**DANKE!**
