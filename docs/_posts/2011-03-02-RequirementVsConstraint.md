---
title: Requirement vs. Constraint
---

Ein Requirement ist eine durch andere Requirements vorgegebenes
Verhalten, Aktion oder Ausprägung.

Ein Constraint sind Einschränkungen auf den Lösungsraum eines Requirements.
Constraints sind daher immer einem oder mehreren Requirements zugeordnet.
Constraints vererben sich (üblicherweise) von dem direkt zugeordneten
Requirement auf alle davon abhängigen Requirements.  Constraints sind (in
Massen) automatisch verifizierbar.


Beipiel: Es soll ein digitales Thermometer desinged werden, dass 
Beschleunigungen von 7G verträgt.

    Name: Thermometer
    Solved by: Anzeige Gehäuse Temperaturfühler Elektronik
     Energieversorgung
    Constraints: BeschleunigungMax7G

Hier vererbt sich die Eigenschaft (Constraint) auf alle Einzelteile.

Falls z.B. aus früheren Projekten ein Gehäuse existiert, welches aber
nur maximal 5G Beschleunigung vertägt, und hier eingesetzt werden
soll, führt dieses zum Konflikt.

    Name: Gehäuse A
    Solved by: ...
    Constraints: BeschleunigungMax5G

Ziel für rmtoo ist die automatische Überprüfung derartiger
Eigenschaften und Detektion möglicher Konflikte.
