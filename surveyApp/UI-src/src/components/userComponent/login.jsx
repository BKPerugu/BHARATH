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

class Login extends Component {
  render() {
    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <Col md={4}>
              <Card
                title="Login"
                content={
                  <form>
                    <FormInputs
                      ncols={["col-md-12"]}
                      proprieties={[
                        {
                          label: "Email",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Please Enter Email",
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

                    <Link to="/survey">
                      <Button bsStyle="info" pullRight fill type="button">
                        Login
                      </Button>
                    </Link>
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

export default Login;
