celcius = int(input("Enter a number: "))        #ile chcemy wpisać stopni w celciuszu

kelwin = celcius + 273,15       #przeliczamy celciusza na kelvina  

farenheit = (celcius * 9/5) + 32  #przeliczamy celciusza na farenheita

temperature = (f"It's {celcius} degrees in Celcius, also it's {kelwin} deegres in kelvin, and it's {farenheit} degrees in farenheit")   #przypisujemy zmienną "temperature" i używamy funkcji f string aby wrzucić przypisane powyższe wartości zmiennych
print(temperature)      #otrzymujemy wynik z powyższej linijki




