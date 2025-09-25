const form = document.getElementById("url-form");
const result = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const url = document.getElementById("url-input").value;

    try {
        const response = await fetch('YOUR_API_GATEWAY_URL', {
            method: 'POST',
            headers: {'content-type': 'application/json'},
            body: JSON.stringify({ url })
        });

        const data = await response.json();
        result.textContent = `Short URL: ${data.shortUrl}`;
    } catch (error) {
       
        result.textContent = 'Error: Could not shorten URL';

    }
});
