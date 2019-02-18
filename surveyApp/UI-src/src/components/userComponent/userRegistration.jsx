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
import CustomCheckbox from "../CustomCheckbox/CustomCheckbox";
import { Link } from "react-router-dom";
import avatar from "../../assets/img/faces/face-3.jpg";

class UserRegistraion extends Component {
  render() {
    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <Col md={4}>
              <Card
                title="Registration"
                content={
                  <form>
                    <FormInputs
                      ncols={["col-md-12"]}
                      proprieties={[
                        {
                          label: "Name",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Please Enter Name",
                          defaultValue: ""
                        }
                      ]}
                    />
                    <div class="form-group">
                      <label for="exampleInputPassword1">Password</label>
                      <input
                        type="password"
                        class="form-control"
                        id="exampleInputPassword1"
                        placeholder="Password"
                      />
                    </div>
                    <div class="form-group">
                      <label for="ConfirmPassword">Confirm Password</label>
                      <input
                        type="password"
                        class="form-control"
                        id="ConfirmPassword"
                        placeholder="Confirm Password"
                      />
                    </div>
                    <form>
                      <label>Have you taken calibration training?</label>
                      <p />
                      <label class="radio-inline">
                        <input type="radio" name="optradio" checked />
                        Yes
                      </label>
                      <label class="radio-inline">
                        <input type="radio" name="optradio" />
                        No
                      </label>
                    </form>
                    <FormInputs
                      ncols={["col-md-12"]}
                      proprieties={[
                        {
                          label: "Location",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Please Enter Location",
                          defaultValue: ""
                        }
                      ]}
                    />

                    <Link to="/userlogin">Go to login</Link>
                    <Link to="/survey">
                      <Button bsStyle="info" pullRight fill type="button">
                        Register
                      </Button>
                    </Link>
                    {/* <Button bsStyle="info" pullRight fill type="submit">
                      Register
                    </Button> */}
                    <div className="clearfix" />
                  </form>
                }
              />
            </Col>
          </Row>
        </Grid>
        >
      </div>
    );
  }
}

export default UserRegistraion;
