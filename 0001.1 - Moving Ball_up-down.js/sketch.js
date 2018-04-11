var y,d
function setup ()
{
createCanvas (500,500);
background (0);
y = 1;
d = 0;
}

function draw()
{
    clear();
    ellipse (250,y,20,20);

    if (y<0)
    {
        d=0;
    }

    if (d==0)
    {
        y++
    }
    if (y>width)
    {
        d=1;
    }

    if (d==1)
    {
        y--
    }
}
