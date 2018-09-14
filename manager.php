<?php
/****************************************************************************
*                                                                           *
* When defining form in html, use <form action="manager.php" method="post"  *
*                               Example:                                    *
*  <form action="manager.php" method="post">                                *
*   What color do you want to see? <input type="text" name="prefColor"      *
*   <input type="submit">                                                   *
*   </form>                                                                 *
*                                                                           *
*****************************************************************************/

    // If the server's method of receiving information is post...
    // We will be using post in the form rather than get
    if ($_SERVER["REQUEST_METHOD"] == "POST"){
        // Going off the color example, this variable will get the color
        $color = $_REQUEST['prefColor'];
        $user_IP = $_SERVER['REMOTE_ADDR'];

        // If the color variable is empty...
        if(empty($color)) {

            // Echo that there was no input
            echo "No color received.";
        }

        // If the color variable isn't empty...
        else {
            // Open a file of given name.
            $myfile = fopen("filename.txt", 'a') or die("invalid file. check input");

            // Write the response from color to the file, add a new line
            // Added arbitrary separators for consistency when splitting in analysis
            // Separators are different to manage responses
            $response = $user_IP + "~;~" + $color + "**^**" + "\n";
            fwrite($myfile, $response);

            // Close the file
            fclose($myfile);
        }
  }
?>
