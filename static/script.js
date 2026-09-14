console.log("AI Workout Coach JavaScript loaded");


// ==========================================
// UPDATE LIVE STATS
// ==========================================

async function updateStats() {

    try {

        const response = await fetch("/stats", {
            cache: "no-store"
        });

        if (!response.ok) {
            throw new Error("Stats request failed");
        }

        const data = await response.json();


        // --------------------------------------
        // REPS
        // --------------------------------------

        const repsElement =
            document.getElementById("reps");

        if (repsElement) {
            repsElement.textContent = data.reps;
        }


        const sessionRepsElement =
            document.getElementById("session-reps");

        if (sessionRepsElement) {
            sessionRepsElement.textContent = data.reps;
        }


        // --------------------------------------
        // ANGLE
        // --------------------------------------

        const angleElement =
            document.getElementById("angle");

        if (angleElement) {

            angleElement.textContent =
                data.angle + "°";
        }


        // --------------------------------------
        // STAGE
        // --------------------------------------

        const stageElement =
            document.getElementById("stage");

        if (stageElement) {

            const stage =
                data.stage.charAt(0).toUpperCase()
                +
                data.stage.slice(1);

            stageElement.textContent = stage;
        }


        // --------------------------------------
        // FORM STATUS
        // --------------------------------------

        const formStatusElement =
            document.getElementById("form-status");

        if (formStatusElement) {

            formStatusElement.textContent =
                data.form_status;
        }


        // --------------------------------------
        // FORM MESSAGE
        // --------------------------------------

        const formMessageElement =
            document.getElementById("form-message");

        if (formMessageElement) {

            formMessageElement.textContent =
                data.form_message;
        }


        // --------------------------------------
        // FORM ICON
        // --------------------------------------

        const formIconElement =
            document.getElementById("form-icon");

        if (formIconElement) {

            if (data.form_score >= 90) {

                formIconElement.textContent = "✓";

            } else if (data.form_score >= 75) {

                formIconElement.textContent = "!";

            } else {

                formIconElement.textContent = "×";
            }
        }

    }

    catch (error) {

        console.error(
            "Stats error:",
            error
        );

    }
}


// ==========================================
// SELECT ARM
// ==========================================

async function selectArm(arm) {

    try {

        const response = await fetch(
            "/select_arm",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    arm: arm
                })
            }
        );


        const data =
            await response.json();


        if (!data.success) {

            console.error(
                "Could not change arm:",
                data.message
            );

            return;
        }


        // --------------------------------------
        // Update active button
        // --------------------------------------

        const rightButton =
            document.getElementById("right-arm");

        const leftButton =
            document.getElementById("left-arm");


        rightButton.classList.remove(
            "active"
        );

        leftButton.classList.remove(
            "active"
        );


        if (arm === "right") {

            rightButton.classList.add(
                "active"
            );

        } else {

            leftButton.classList.add(
                "active"
            );
        }


        console.log(
            "Tracking:",
            arm,
            "arm"
        );

    }

    catch (error) {

        console.error(
            "Arm selection error:",
            error
        );

    }
}


// ==========================================
// START LIVE UPDATES
// ==========================================

setInterval(
    updateStats,
    100
);

updateStats();