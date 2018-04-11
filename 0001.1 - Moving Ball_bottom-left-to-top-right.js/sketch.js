var x,y,d
function setup ()
{
createCanvas (500,500);
background (0);
x = 250;
y = 250;
d = 1;
}

function draw()
{
    clear();
    ellipse (x,y,20,20);

    if (d==1)
    {
        x++;
        y--;
    }

    if (d==0)
    {
        x--;
        y++;
    }

    if ((x==500) && (y==0))
    {
        d=0;
    }


    if ((x==0) && (y==500))
    {
        d=1;
    }
}
