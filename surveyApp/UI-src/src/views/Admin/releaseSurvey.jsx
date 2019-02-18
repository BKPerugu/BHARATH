import React, { Component } from "react";
import {
  Grid,
  Row,
  Col,
  FormGroup,
  ControlLabel,
  FormControl
} from "react-bootstrap";

import { Card } from "../../components/Card/Card.jsx";
import { FormInputs } from "../../components/FormInputs/FormInputs.jsx";

import Button from "../../components/CustomButton/CustomButton.jsx";

class ReleseSurvey extends Component {
  render() {
    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <Col md={8}>
              <Card
                title="Survey Upload"
                content={
                  <form>
                    <div class="form-group">
                      <label for="sel3">Company Name</label>
                      <select class="form-control" id="sel3">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label for="sel1">Survey Name</label>
                      <select class="form-control" id="sel1">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label for="sel2">Department Name</label>
                      <select multiple class="form-control" id="sel2">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                      </select>
                    </div>
                    <div>
                      <Button bsStyle="info" pullRight fill type="submit">
                        Release Survey
                      </Button>
                    </div>
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

export default ReleseSurvey;
