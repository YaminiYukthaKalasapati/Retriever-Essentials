document.getElementById('start-scan').addEventListener('click', function() {
    console.log("Initializing scanner...");
    Quagga.init({
        inputStream: {
            type: "LiveStream",
            target: document.querySelector('#barcode-scanner'),
            constraints: {
                width: 640,
                height: 480,
                facingMode: "environment"
            }
        },
        decoder: {
            readers: ["upc_reader", "code_128_reader", "ean_reader", "ean_8_reader", "code_39_reader", "i2of5_reader"]
        }
    }, function(err) {
        if (err) {
            console.error("Quagga initialization error:", err);
            return;
        }
        console.log("Quagga initialized successfully");
        Quagga.start();
    });

    Quagga.onDetected(function(result) {
        var barcode = result.codeResult.code;
        console.log("Detected Barcode:", barcode);

        // Fetch item details from the server based on the barcode
        fetch(`/inventory/get-item-details/?barcode=` + barcode)
            .then(response => response.json())
            .then(data => {
                console.log("Data fetched from server:", data);
                if (data.status === 'success') {
                    // Populate form fields
                    document.querySelector('input[name="name"]').value = data.item.name;
                    document.querySelector('textarea[name="description"]').value = data.item.description;
                    document.querySelector('input[name="quantity"]').value = data.item.quantity;
                    document.querySelector('input[name="price"]').value = data.item.price;
                    document.querySelector('input[name="barcode"]').value = barcode;
                    document.querySelector('select[name="category"]').value = data.item.category;
                } else {
                    alert(data.message);
                }
            })
            .catch(error => console.error("Error fetching item details:", error));

        Quagga.stop();  // Stop scanning after detection
    });
});
