1. Schreibe das XPath für das im untenstehenden Bild hervorgehobene Symbol/den hervorgehobenen Button.  
(//div[@class = 'headerIcon'])[1]
    
    

2. Öffne nun https://grocerymate.masterschool.com/auth.
Schreibe das **XPath** für **alle Eingabefelder**, die **"Sign In"**-Schaltfläche, den Link **"Create a new account"** und den Link **"Go to Home"**.  
Email: //form[@class = 'form']//input[@type = 'email']  
Password: //form[@class = 'form']//input[@type = 'password']  
Sign-In-Button: //form[@class = 'form']//button[@type = 'submit']  
Create-New-Account-Link: //form[@class = 'form']//a[@class = 'switch-link']  
Go-To-Home-Link: //form[@class = 'form']//a[@class = 'home-link']  


3. Klicke nun auf denselben Link wie in Teil 2 auf **"Create a new account"**.
Schreibe das **XPath** für **alle Eingabefelder** und die **"Sign Up"**-Schaltfläche.  
Full Name: //form[@class = 'form']//input[@type = 'text']  
Email: //form[@class = 'form']//input[@type = 'email']  
Password: //form[@class = 'form']//input[@type = 'password']  
Sign-Up-Button: //form[@class = 'form']//button[@type = 'submit']  
Already-Registered-Link: //form[@class = 'form']//a[@class = 'switch-link']  
Go-To-Home-Link: //form[@class = 'form']//a[@class = 'home-link']    


4. Gehe zu https://grocerymate.masterschool.com/store
Schreibe das **XPath** der **"Confirm"**-Schaltfläche, die du im Modal sehen kannst.  
//div[@class = 'modal-content']//button  


5. Gehe zur **Shop-**Seite und schreibe das **XPath** für das **Mengeneingabefeld von Orangen**, die **"Add to cart"**Schaltfläche für Orangen und die **"Add to wish list"**Schaltfläche für Orangen.  
Mengeneingabe: //div[@class='card-header'][p/text()='Orange']/following-sibling::div//div[@class = 'col-3']  
Add-to-cart-Button: //div[@class='card-header'][p/text()='Orange']/following-sibling::div//div[@class = 'col-7']  
Add-to-wishlist-Button: //div[@class='card-header'][p/text()='Orange']/following-sibling::div//div[@class = 'col-1']  