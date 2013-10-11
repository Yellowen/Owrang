$(document).ready(function() {
    $(".navbar, footer, .banner, #user-tools").toggle(false);
    
    $("#login_btn").click(function() {
        var me = this;
        $(this).html("Logging In...").prop("disabled", true);
        wn.call({
            "method": "login",
            args: {
                usr: "demo@owrang.yellowen.com",
                pwd: "demo",
                lead_email: $("#lead-email").val(),
            },
            callback: function(r) {
                $(me).prop("disabled", false);
                if(r.exc) {
                    alert("Error, please contact support@owrang.yellowen.com");
                } else {
                    console.log("Logged In");
                    window.location.href = "app.html";
                }
            }
        })
        return false;
    })
    .prop("disabled", false);
})