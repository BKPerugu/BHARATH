import React, { Component } from "react";
import {
  Grid,
  Row,
  Col,
  FormGroup,
  ControlLabel,
  FormControl
} from "react-bootstrap";

import { Card } from "../Card/Card.jsx";
import { FormInputs } from "../FormInputs/FormInputs.jsx";
import { UserCard } from "../UserCard/UserCard.jsx";
import Button from "../CustomButton/CustomButton.jsx";
import { Link } from "react-router-dom";
import avatar from "../../assets/img/faces/face-3.jpg";

class UserProfile extends Component {
  render() {
    return (
      <React.Fragment>
        <div className="content">
          <Grid fluid>
            <Row>
              <Col md={4}>
                <Card
                  title=" Validate & Login"
                  content={
                    <form>
                      <FormInputs
                        ncols={["col-md-12"]}
                        proprieties={[
                          {
                            label: "Email Id",
                            type: "text",
                            bsClass: "form-control",
                            placeholder: "Please Enter Email",
                            defaultValue: ""
                          }
                        ]}
                      />
                      <FormInputs
                        ncols={["col-md-12"]}
                        proprieties={[
                          {
                            label: "company Name",
                            type: "text",
                            bsClass: "form-control",
                            placeholder: "Please Enter company Name",
                            defaultValue: ""
                          }
                        ]}
                      />
                      <FormInputs
                        ncols={["col-md-12"]}
                        proprieties={[
                          {
                            label: "Department",
                            type: "text",
                            bsClass: "form-control",
                            placeholder: "Please Enter Department Name",
                            defaultValue: ""
                          }
                        ]}
                      />

                      <Link to="/userregistration">
                        <Button bsStyle="info" pullLeft fill type="button">
                          Validate & Login
                        </Button>
                      </Link>

                      <div className="clearfix" />
                    </form>
                  }
                />
              </Col>
            </Row>
          </Grid>
        </div>
      </React.Fragment>
    );
  }
}

export default UserProfile;
