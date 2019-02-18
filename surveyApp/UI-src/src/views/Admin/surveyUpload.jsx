import React, { Component } from "react";
import {
  Grid,
  Row,
  Col,
  FormGroup,
  ControlLabel,
  FormControl
} from "react-bootstrap";
import axios from "axios";
import { Card } from "../../components/Card/Card.jsx";
import { surveyUpload } from "../../services/adminService";
class SurveyUpload extends Component {
  state = {
    data: {
      Survey_name: "",
      company_name: "",
      file_name: ""
    }
  };
  handleselectedFile = event => {
    console.log(event);
 
    const data = { ...this.state.data };
    data[event.target.id] = event.target.files[0].name;
    this.setState({
      data
    });
    const formData = new FormData();

  formData.append("file", event.target.files[0]);

  axios
    .post("http://127.0.0.1:5000/questionsUpload", formData)
    .then(res => console.log(res));
  };
  handleChange = ({ currentTarget: input }) => {
    const data = { ...this.state.data };
    data[input.name] = input.value;
    this.setState({ data });
  };
  doSubmit = async () => {
    await surveyUpload(
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
                title="Survey Upload"
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
                      <label for="exampleFormControlFile1">Upload Survey</label>
                      <input
                        type="file"
                        class="form-control-file"
                        id="exampleFormControlFile1"
                        onChange={this.handleselectedFile}
                      />
                    </div>

                    <button
                      className="btn-fill pull-right btn btn-info"
                      type="button"
                      onClick={this.doSubmit}
                    >
                      Upload Survey
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

export default SurveyUpload;
