var y,x,Am
function setup() {
    createCanvas(600,600);
    background(200);
    strokeWeight(5);
    x = 0; // time
    Am = 200;//amplitude
}

function draw() {
    point(x,y);
    y = Am * sin(2*3.14*10*x) + 300 ; //300 fixes x-axis in the centre
    x = x+1;
}
