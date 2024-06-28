# TR
## The Elder Scrolls Online Dil Dosyaları Güncelleme Yardımcısı
The Elder Scrolls Online'da oyuna eklenen, silinen veya değiştirilen satırlarda yapılması gereken değişiklikleri kolaylaştıran ve belgeleri EsoExtractData'da kullanılmak üzere hazırlayan yardımcı bir araçtır.

## Bu programla neler yapılabiliyor ?
Oyunda yeni güncelleme yayınlandığında yeni dil dosyaları ve üzerlerinde yapılan değişiklikleri görebileceğiniz belgeleri paylaşan bir site mevcut : [Unofficial Elder Scrolls Pages](https://esofiles.uesp.net/) 

Son güncelleme ile gelen dosyalar arasında client, pregame, lang ve diff dosyaları bulunuyor. Bu program bu dosyalarla herhangi bir text editor kullanılarak yapılması gereken işlemleri kolayca gerçekleştirebiliyor. Bu işlemler şunlar :
- en.diff.txt dosyasında oyundaki eklenen,silinen ve değiştirilen satırları ayrı dosyalara ayırabilir ve ID formatını düzenleyebilir
- en.diff.txt dosyasında "Deleted" yazılı oyundan çıkarılmış satırları tb.lang.txt ile kıyaslayarak silebilir
- en.diff.txt dosyasında "Changed" yazılı oyundaki değiştirilmiş satırları tb.lang.txt ile kıyaslayarak değiştirebilir
- ID'si bulunmayan, çevirisi yapılmış satırların başına tekrar ID ekleyebilir
- Satırların başındaki ID'leri silebilir
- Sadece satırların başındaki ID'leri kaydedebilir
- en.diff.txt'de belirtilmiş, güncelleme ile oyuna yeni eklenen satırları tb.lang.txt ile birleştirebilir ve sıralayabilir.
- Client ve pregame.lua dosyalarındaki yeni eklenmiş satırları .str dosyası ile karşılaştırabilir ve eksik ya da silinmiş satırları bularak yeni dosyalara kaydedebilir

## Programlar Klasörü

Yukarıda belirttiğim işlemleri gerçekleştiren her bir programın kodlamasını bu klasörde bulabilirsiniz. Kodlamalar yapay zeka yardımıyla oluşturuldu. Hangi kodun ne işe yaradığını açıklayan satırlar da mevcut.

## Kurulum

- Programı [buradan](https://github.com/Balgamov/ESO-Lang-Update-Helper/releases) indirebilirsiniz.
- Programların çalışması için [Python](https://www.python.org/downloads/) gerekiyor.
- TSOLangHelper.exe 'yi çalıştırın. Bu kadar :)

## Kullanım

Programı çalıştırdıktan sonra sağ tarafta bulunan Örnek düğmelerini kullanarak gerçekleştireceğiniz işlem hakkında daha detaylı bilgi edinebilirsiniz.

![TSO](https://github.com/Balgamov/ESO-Lang-Update-Helper/assets/134242131/12ebe0ea-120e-439d-b221-ac49ab74691e)



# EN
## The Elder Scrolls Online Language Files Update Helper
It is a helpful tool that facilitates the changes that need to be made to lines that ESO has added, deleted or changed in the game and to prepare documents for use in EsoExtractData.

## What can I do with this software?
When a new update is released in the game, there is a website that shares documents where you can see the new language files and the changes made to them: [Unofficial Elder Scrolls Pages](https://esofiles.uesp.net/)


The files that came with the latest update include client, pregame, lang and diff files. This program can easily perform operations that need to be done with these files using any text editor. These operations are as follows:
- In the en.diff.txt file, it can separate the added, deleted and changed lines in the game into separate files and edit the ID format
- In the en.diff.txt file, it can delete the lines that are removed from the game with the text "Deleted" by comparing them with tb.lang.txt
- In the en.diff.txt file, it can change the modified lines in the game written "Changed" in the en.diff.txt file by comparing it with tb.lang.txt
- Can add IDs again to the beginning of translated lines that do not have an ID
- Can delete the IDs at the beginning of the lines
- Can only save the IDs at the beginning of the lines
- Can combine and sort the lines specified in en.diff.txt that were newly added to the game with the update with tb.lang.txt. 
- Can compare newly added lines in client and pregame.lua files with .str file and find missing or deleted lines and save them to new files

## Programlar Folder

You can find the coding of each program that performs the operations I mentioned above in this folder. The codings were created with the help of AI. There are also lines explaining what each code does.

## Install

- You can download the program from [here](https://github.com/Balgamov/ESO-Lang-Update-Helper/releases).
- The programs require [Python](https://www.python.org/downloads/) to run.
- Run TSOLangHelper.exe , that's it :)

## Usage

After running the program, you can get more detailed information about the operation you will perform by using the Example buttons on the right side.

![TSOEN](https://github.com/Balgamov/ESO-Lang-Update-Helper/assets/134242131/ed186e20-4340-4c2d-99d9-223961304a47)


