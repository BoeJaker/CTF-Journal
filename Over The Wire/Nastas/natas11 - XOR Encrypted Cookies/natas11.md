# Natas 11 XOR Cipher

# Step 1 - Grab the cookie

# Step 2 - Generte Key

    <?php

    function xor_encrypt($in) {
        $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
        $text = $in;
        $outText = '';

        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }
    $results = xor_encrypt(base64_decode('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSh4bjY'));
    print($results)
    ?>

# Step 3 - Double check by using the key to decode our cookie
    <?php

    function xor_encrypt($in) {
        $key = "KNHL";
        $text = $in;
        $outText = '';

        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }
    $results = xor_encrypt(base64_decode('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSh4bjY'));
    print($results)
    ?>

# Step 4 - use the key to bake a new cookie with the showpassword parameter set to yes.
    <?php

    function xor_encrypt($in) {
        $key = "KNHL";
        $text = $in;
        $outText = '';

        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }
    $results = base64_encode(xor_encrypt(json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"))));
    print($results)
    ?>

# Step 5 - Use a cookie editor to insert our newly baked cookies

# Step 6 - Reload the page to see the password for the next level