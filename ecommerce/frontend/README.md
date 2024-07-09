# Thanks for visiting ModernMonarch® 😃

## What is ModernMonarch®?
ModernMonarch is a website that i built where user can come in and buy clothes! I built this website using React as my frontend and Django for my backend.  
I implemented an API using react to fetch data from my django backend by using **asynchronous functions.** Asynchronous functions do not return promises like  
regular functions. They wait for something to happpen and then they execute. An example of an **asynchronous function** would be this:  


```javascript
const fetchCart = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/get_cart_items/", {
        credentials: "include",
      });
      const cartData = await response.json();
      console.log("Fetched cart data:", cartData);
      setCart(cartData);
    } catch (error) {
      console.error("Error fetching cart data:", error);
    }
  };
```
In this example my frontend is talking to my backend using the URL above and asking it for the items that are being added from the backend. After my react component gets this information, then I would be able to render it to the user on the UI.


## Challenges
This project really helped me understand how frontend and backend communicate with eachother. Building this app was really fun but challenging.  
After not building apps with Django in a long time I really had to go back and relearn the syntax. There was also things I didn't know how to do so I had to do a lot of research to get things working. 

Some of those things that I really struggled with was deleting items from the cart one by one and adding serializers. I reasearched what serializers were and found that serializers are Django models that you are converting into JSON. If you do not do this then you cannot render anything in the front end. I had to learn this the hard way...

I was able to get a lot of help from **ChatGPT** and **Claude AI**. It's nice to be able to use these resources but you still need to understand the solution that its giving you. There was times where these tools would spit something out and I had no idea what the code was, so I had them break it down line by line. That helped me wrap my head around things such as the functions for removing items from the cart one by one.