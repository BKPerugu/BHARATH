import React from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import { Grid, Row, Col } from "react-bootstrap";
import "react-tabs/style/react-tabs.css";
import Card from "../../components/Card/Card.jsx";
import MyClickable from "./hello";
import MyClickableQutions from "./hellotest";
import { Link } from "react-router-dom";
import "./user.css";
import {
  RadioGroup,
  RadioButton,
  ReversedRadioButton
} from "react-radio-buttons";
import Button from "../CustomButton/CustomButton.jsx";
export class SurveyList extends React.Component {
  state = {
    activeIndex: null,
    activeIndexQutions: null,
    activeIndexQutions2: null,
    resiliencequality: ""
  };

  handleClick = index => this.setState({ activeIndex: index });
  onChange = event => {
    this.setState({ resiliencequality: event });
  };
  handleQutionsClick = index => this.setState({ activeIndexQutions: index });
  handleQutionsClick2 = index => this.setState({ activeIndexQutions2: index });
  showConfidence = () => {
    if (
      this.state.resiliencequality === "Poor" ||
      this.state.resiliencequality === "Fair" ||
      this.state.resiliencequality === "Good"
    )
      return (
        <RadioGroup horizontal>
          <RadioButton value="Slight">Slight</RadioButton>
          <RadioButton value="Moderate">Moderate</RadioButton>
          <RadioButton value="High">High</RadioButton>
        </RadioGroup>
      );
  };
  showtheGrid = () => {
    if (this.state.activeIndex != null)
      return (
        <Row>
          <Col md={12}>
            <Card
              title="Take Survey"
              category=""
              content={
                <div>
                  <div>
                    <h3>
                      1.How likely is it that you would recommend this company
                      to a friend or collegue?
                    </h3>
                  </div>
                  <div
                    className="btn-group mr-2"
                    role="group"
                    aria-label="First group"
                  >
                    <MyClickable
                      name="1"
                      index={4}
                      isActive={this.state.activeIndexQutions === 4}
                      onClick={this.handleQutionsClick}
                    />
                    <MyClickable
                      name="2"
                      index={5}
                      isActive={this.state.activeIndexQutions === 5}
                      onClick={this.handleQutionsClick}
                    />
                    <MyClickable
                      name="3"
                      index={6}
                      isActive={this.state.activeIndexQutions === 6}
                      onClick={this.handleQutionsClick}
                    />
                    <MyClickable
                      name="4"
                      index={7}
                      isActive={this.state.activeIndexQutions === 7}
                      onClick={this.handleQutionsClick}
                    />
                    <MyClickable
                      name="5"
                      index={12}
                      isActive={this.state.activeIndexQutions === 12}
                      onClick={this.handleQutionsClick}
                    />
                  </div>
                  <div>
                    <div>
                      <h3>2.How likely this application?</h3>
                    </div>
                    <div
                      className="btn-group mr-2"
                      role="group"
                      aria-label="First group"
                    >
                      <MyClickable
                        name="1"
                        index={8}
                        isActive={this.state.activeIndexQutions2 === 8}
                        onClick={this.handleQutionsClick2}
                      />
                      <MyClickable
                        name="2"
                        index={9}
                        isActive={this.state.activeIndexQutions2 === 9}
                        onClick={this.handleQutionsClick2}
                      />
                      <MyClickable
                        name="3"
                        index={10}
                        isActive={this.state.activeIndexQutions2 === 10}
                        onClick={this.handleQutionsClick2}
                      />
                      <MyClickable
                        name="4"
                        index={11}
                        isActive={this.state.activeIndexQutions2 === 11}
                        onClick={this.handleQutionsClick2}
                      />
                      <MyClickable
                        name="5"
                        index={13}
                        isActive={this.state.activeIndexQutions2 === 13}
                        onClick={this.handleQutionsClick2}
                      />
                    </div>
                  </div>
                  <p />
                  <Link to="/survey">
                    <Button bsStyle="info" pullLeft fill type="button">
                      Submit
                    </Button>
                  </Link>
                </div>
              }
            />
          </Col>
        </Row>
      );
  };
  render() {
    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <Col md={12}>
              <Card
                title="Survey List"
                category=""
                content={
                  <div>
                    <Tabs>
                      <TabList>
                        <Tab>Physical</Tab>
                        <Tab>Organizational</Tab>
                        <Tab>Technical</Tab>
                      </TabList>

                      <TabPanel>
                        {/* <RadioGroup
                          onChange={event => this.onChange(event)}
                          vertical
                        >
                          <RadioButton value="Poor">Poor</RadioButton>
                          <RadioButton value="Fair">Fair</RadioButton>
                          <RadioButton value="Good">Good</RadioButton>
                          <RadioButton value="Very Good">Very Good</RadioButton>
                          <RadioButton value="Excellent">Excellent</RadioButton>
                        </RadioGroup>
                        {this.showConfidence()} */}
                        <Row>
                          <Col md={12}>
                            <Card
                              title="Select Category"
                              category=""
                              content={
                                <div
                                  className="btn-toolbar"
                                  role="toolbar"
                                  aria-label="Toolbar with button groups"
                                >
                                  <div
                                    className="btn-group mr-2"
                                    role="group"
                                    aria-label="First group"
                                  >
                                    <MyClickable
                                      name="Category1"
                                      index={0}
                                      isActive={this.state.activeIndex === 0}
                                      onClick={this.handleClick}
                                    />
                                    <MyClickable
                                      name="Category2"
                                      index={1}
                                      isActive={this.state.activeIndex === 1}
                                      onClick={this.handleClick}
                                    />
                                    <MyClickable
                                      name="Category3"
                                      index={2}
                                      isActive={this.state.activeIndex === 2}
                                      onClick={this.handleClick}
                                    />
                                    <MyClickable
                                      name="Category4"
                                      index={3}
                                      isActive={this.state.activeIndex === 3}
                                      onClick={this.handleClick}
                                    />
                                  </div>
                                </div>
                              }
                            />
                          </Col>
                        </Row>
                      </TabPanel>
                      <TabPanel>
                        <h2>Any content 2</h2>
                      </TabPanel>
                      <TabPanel />
                    </Tabs>
                  </div>
                }
              />
            </Col>
          </Row>
          {this.showtheGrid()}
        </Grid>
      </div>
    );
  }
}
export default SurveyList;
