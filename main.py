while True:
    print('Das ist das Naturschutz Quiz. Willst du teilnehmen?')

    teilnehmen = input('Willst du teilnehmen? ja/nein?\n')

    if teilnehmen == 'nein':
      print ('programm beenden...')
      break

    ja_count = 0  # Setze ja_count zu Beginn auf 0

    print('Ok, die Regeln sind folgende:')
    
    print ('1.Ich werde dir jetzt 10 Tierfakten nennen und du sagst mir ob du die schon kanntest.')
    print('2. Du darfst nur mit ja und nein antworten.')
    

    bereit = input('Also, bist du bereit? ja/nein?\n')

    if bereit == 'nein':
       print ('Programm beenden...')
       break

    # 1. Frage
    print('1. Wusstest du, dass Tintenfische 3 Herzen haben?')

    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
  
    

    # 2. Frage
    print('2.Wusstest du, dass Faultiere einen Monat brauchen, um ein einziges Blatt zu verdauen?')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
    # 3. Frage
    print('3.Wusstest du, dass Eisbären nicht wirklich weiß sind? Eigentlich haben sie schwarze Haut unter ihrem Fell.')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
    # 4. Frage
    print('4.Wusstest du, dass Elefanten die einzigen Säugetiere sind, die nicht springen können?')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
    # 5. Frage
    print('5.Wusstest du, dass Kolibris die einzigen Vögel sind, die rückwärts fliegen können?')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
    # 6. Frage
    print('6.Wusstest du, dass der Blauwal das größte Herz aller Tiere hat? Fun Fact es ist so groß wie ein kleines Auto.')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
    # 7. Frage
    print('7.Wusstest du, dass Ameisen zwar viele kleine Ruhepausen über den Tag machen, aber nie schlafen?')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
    # 8. Frage
    print('8.Wusstest du, dass Seesterne zwar ein komplexes Nervensystem, aber kein Gehirn haben?')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
    # 9. Frage
    print('9.Wusstest du, dass Kraken sich durch jeden Spalt quetschen können, der so groß ist wie ihr Schnabel?')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1
    # 10. Frage
    print('10.Wusstest du, dass Giraffen kaum Laute von sich geben, da sie durch ihre langen Hälse nicht genügend Luftdruck für Töne erzeugen können?')
    antwort =      input('ja/nein\n').strip().lower()

    if antwort == 'ja':
     ja_count += 1

    print('Und die Auswertung ist:')

    if ja_count == 10:
        print('Wow du kanntest alle Fakten. Du weißt echt richtig viel über Tiere. Geh doch mal zum Zoo und bewerbe dich auf eine Stelle.\n')
    elif ja_count == 5:
        print('Du kanntest fünf Fakten. Du bist schon ganz gut informiert aber es geht bestimmt noch besser.\n')
    elif ja_count == 0:
        print('Du wusstest nicht mal einen Fakt. Bitte informiere dich mehr über das Thema.\n')
    elif ja_count == 1:
        print ('Du kanntest gerade einmal einen Fakt. Mehr kann man dazu eigentlich nicht sagen.\n')
    elif ja_count == 2:
        print ('Du kanntest nur 2 Fakten. Informiere dich bitte mehr.\n')
    elif ja_count == 3:
        print ('Du hattest gerade einmal 3 Fakten richtig. Ein bisschen mehr informieren ist bestimmt nicht so schwer.\n')
    elif ja_count == 4:
        print ('Du kanntest schon 4 Fakten. Aber ein bisschen mehr geht noch.\n')
    elif ja_count == 6:
        print ('Gut gemacht du wusstest 6 Fakten. Du kennst dich gut aus.\n')
    elif ja_count == 7:
        print ('Du weißt schon ganze 7 Fakten. Du weißt echt viel.\n')
    elif ja_count == 8:
        print ('Du kennst ganze 8 Fakten. Jetzt kannst du dich wirklich einen Tierkenner nennen.\n')
    elif ja_count == 9:
        print ('Wow du hattest 9/10 Fakten richtig. Du weißt echt richtig viel.\n')
      

    break