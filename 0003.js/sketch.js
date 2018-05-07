var x, y, r, A
function setup(){
createCanvas (500,500);
background (67);
r = 225;
A = 0;
//let initial location be 250,250, so x = 250, y = 250;
}
function draw (){
    clear ();
    background (67);
    ellipse(250,250,3,3);//centre
    //x = r cos a and y = r sin a ; as per trigonometry :)
    A = A+25;
    ellipse((250+ r*cos(A)),(250+r*sin(A)),25,25);
}
