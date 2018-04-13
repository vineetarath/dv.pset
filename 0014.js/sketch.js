var n, val;
var input, button, question;

function setup()
{
    createCanvas(450,750);//create canvas

    question = createElement('h2','You desperately ;p seek the Factorial of?' ); //i suppose h2 is header 2
    question.position(30,0);//question location

    input = createInput();
    input.position(30,60);//input location

    //textAlign(CENTER);<----i wonder what this is/was doing
    //textSize(30);

    button = createButton('Please help me with the true answer:)!');//button label ;)
    button.position(30,90);//button location
    button.mousePressed(greet);//call function greet
}

function greet()
{
    var n = input.value();//take input value of n

    //input.value('');//<----why did we do this?

    for(val=n-1;val>0;val--)//THE 'FOR' FUNCTION!
    {
        n = n*val;
        print (n);
    }
    question.html('Help has arrived love! The factorial is ' +n+ ' :*!');
    question.position(30,100);
}
