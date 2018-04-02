var x,d
function setup ()
{
    createCanvas(500,500);
    x=12.5;
    d=0;
}

function draw()
{
    clear ();
    background(44);
    ellipse (x,250,25,25);
    //let leftmost edge be defined by d = 1,
    if (x<=12.5)
    {
        d = 1;
    }
    //let rightmost edge be defined by d = 0,
    if (x>=500-12.5)
    {
        d = 0;//move left; d = 0 is rightmost edge
    }

    //if d = 0, i.e. d has reached rightmost edge, start moving left
    if (d == 0)
    {
        x = x-1;
    }
    //if d = 1, i.e. d has reached leftmost edge, start moving right
    if (d == 1)
    {
        x = x+1;
    }
}
