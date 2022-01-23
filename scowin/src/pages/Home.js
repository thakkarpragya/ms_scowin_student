import React, { Fragment } from 'react';
import './style.css';
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';

<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
  integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
  crossorigin="anonymous"
/>

export default function Home() {
  return (
    <Fragment>
      <div className="sec">
        <div> 
            <h3 className='home_head'> Overview </h3>
            <CardGroup>
               <Card>
                 <Card.Header>
                    <Card.Link href="#">View Details</Card.Link> 
                 </Card.Header>
                  <hr />
                  <Card.Body>
                    <Card.Title>XXX</Card.Title>
                    <Card.Text>
                      STUDENTS REGISTERED
                    </Card.Text>
                  </Card.Body>
                </Card>
                <Card>
                  <Card.Header>
                    <Card.Link href="#">View Details</Card.Link> 
                  </Card.Header>
                  <hr />
                  <Card.Body>
                    <Card.Title>XXX</Card.Title>
                    <Card.Text>
                        STUDENTS VACCINATED
                    </Card.Text>
                  </Card.Body>
                </Card>
                <Card>
                <Card.Header>
                    <Card.Link href="#">View Details</Card.Link> 
                 </Card.Header>
                  <hr />
                  <Card.Body>
                    <Card.Title>XX %</Card.Title>
                    <Card.Text>
                      PERCENTAGE OF STUDENTS VACCINATED
                    </Card.Text>
                  </Card.Body>
                </Card>
              </CardGroup>
        </div>
      </div>
    </Fragment>
  )
}
