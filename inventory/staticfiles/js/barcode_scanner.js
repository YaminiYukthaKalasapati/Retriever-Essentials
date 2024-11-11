function startScanner() {
    // Initialize the barcode scanning library here
    const video = document.createElement("video");
    const barcodeInput = document.getElementById("barcode");

    // Use a library like QuaggaJS to initialize barcode scanning
    Quagga.init({
        inputStream: {
            name: "Live",
            type: "LiveStream",
            target: video, // Attach the video element here
        },
        decoder: {
            readers: ["code_128_reader"], // specify your barcode format
        },
    }, function(err) {
        if (err) {
            console.log(err);
            return;
        }
        console.log("Initialization finished. Ready to start");
        Quagga.start();
    });

    // Event listener for detected barcode
    Quagga.onDetected(function(result) {
        var code = result.codeResult.code;
        barcodeInput.value = code;
        Quagga.stop(); // Stop after one scan
    });
}
