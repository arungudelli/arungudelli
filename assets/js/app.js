if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch(function (err) {
        console.log('ServiceWorker failed', err);
    });
    
}

<script async src="https://www.googletagmanager.com/gtag/js?id=G-L7BW5PW0L8"></script>

window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-L7BW5PW0L8');
