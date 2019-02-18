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
import { userdataupload } from "../../services/adminService";
class UserUpload extends Component {
  state = {
    data: {
      Survey_name: "",
      company_name: ""
    }
  };
  handleChange = ({ currentTarget: input }) => {
    const data = { ...this.state.data };
    data[input.name] = input.value;
    this.setState({ data });
  };
  doSubmit = async () => {
    await userdataupload(
      this.state.data.Survey_name,
      this.state.data.company_name
    );
  };
  render() {
    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <Col md={8}>
              <Card
                title="User Data Upload"
                content={
                  <form>
                    <div class="row">
                      <div class="col-md-12">
                        <div class="form-group">
                          <label className="control-label">Survey Name</label>
                          <input
                            className="form-control"
                            type="text"
                            placeholder="Enter Survey Name"
                            name="Survey_name"
                            value={this.state.data.Survey_name}
                            label="Survey Name"
                            onChange={this.handleChange}
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-12">
                        <div class="form-group">
                          <label className="control-label">Company Name</label>
                          <input
                            className="form-control"
                            type="text"
                            placeholder="Enter Comapany Name"
                            name="company_name"
                            value={this.state.data.company_name}
                            label="Company Name"
                            onChange={this.handleChange}
                          />
                        </div>
                      </div>
                    </div>
                    <div class="form-group">
                      <label for="exampleFormControlFile1">Upload Users</label>
                      <input
                        type="file"
                        class="form-control-file"
                        id="exampleFormControlFile1"
                      />
                    </div>
                    <button
                      className="btn-fill pull-right btn btn-info"
                      type="button"
                      onClick={this.doSubmit}
                    >
                      Upload Users
                    </button>

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

export default UserUpload;
