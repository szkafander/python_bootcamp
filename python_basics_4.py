# python alapok

# Python telepítése (Windows rendszeren):
# 1. Anaconda letöltése és telepítése: 
#     https://www.anaconda.com/distribution/#download-section
# 2. Spyder IDE elindítása
# 3. Megnyitni ezt a fájlt Spyder-ben
# 4. A fájl cellákból áll. Egy cella két '#%%' közötti szövegrész. Ha a kurzor
#     egy adott cellában villog, akkor azt a cellát a Ctrl+Enter billentryű
#     kombinációval tudjátok futtatni.
# 5. A cellákat egymás után, fentről lefelé haladva érdemes futtatni.

# feladat 1: ahol láttok egy kifejezést egy kettősponttal, oda a kettőspont 
# után írjátok le hogy mit jelent az adott kifejezés, mire jó, és hogyan kell 
# használni. lehetőleg angol nyelven írjatok.
#
# pl.:
#
# import: betölt egy modult, aminek változóit, metódusait és osztályait az
# importálás után használhatjuk. az importálandó modulnak a Python path-en
# megtalálhatónak kell lennie.
#
# feladat 2: minden részt és minden részletet értsetek meg ebből a fájlból.
# miért működik ez a script úgy, ahogy?
#
# a feladat innen angolul van. ezt azért jó megszokni, mert minden 
# internetes forrás is angolul lesz.

#%%
from submodule import script

print("\n", "Saying some more words...", "\n")

# _:
# range:
# for:
for _ in range(10):
    # nested module member:
    script.vocalize.say_something()

# rerun this cell. how many times do you see the 'Saying a word...' text? why?:
# solve the files in the submodule and the submodule/subsubmodule folders
