function showLoading() {

    const button =
        document.getElementById("generate-button");

    const loading =
        document.getElementById("loading");

    if (button) {

        button.disabled = true;

        button.innerHTML =
            "Generating...";
    }

    if (loading) {

        loading.style.display = "block";

    }
}


function previewImage(event) {

    const preview =
        document.getElementById("image-preview");

    if (!preview) {
        return;
    }

    preview.innerHTML = "";

    const file =
        event.target.files[0];

    if (!file) {
        return;
    }

    const image =
        document.createElement("img");

    image.src =
        URL.createObjectURL(file);

    image.className =
        "preview-image";

    preview.appendChild(image);
}


document.addEventListener(
    "DOMContentLoaded",
    function () {

        const alerts =
            document.querySelectorAll(".flash");

        alerts.forEach(
            function (alert) {

                setTimeout(
                    function () {

                        alert.style.opacity = "0";

                        setTimeout(
                            function () {

                                alert.remove();

                            },
                            500
                        );

                    },
                    4000
                );

            }
        );

    }
);