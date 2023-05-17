# Web 相关


- JavaScript的统治地位




```javascript

const add_button = document.createElement("button")
add_button.id = "No1"
add_button.addEventListener('click' = () => operate())


const current_next = document.getElementById("DSD")
functon operate() {
    return "Good"
}


```

- 两种存储：localStorage 和sync Storage，
  - LocalStorage 是存储在本地的，你在自己的浏览器里打开就能用，但在别人的浏览器里打开就用不了了；
  - sync storage 是同步存储，你在一处使用了，换了电脑，重新用上，还在；
  - 是通过key-value pair的方式进行存储的，所以存的时候都是用 `{A:B}`的方式

```javascript
chrome.storage.local.get(['name'], result => {

})
```
