import React, { Component } from "react";
import ChartistGraph from "react-chartist";
import { Grid, Row, Col } from "react-bootstrap";

import { Card } from "../../components/Card/Card.jsx";
import { StatsCard } from "../../components/StatsCard/StatsCard.jsx";
import { Tasks } from "../../components/Tasks/Tasks.jsx";
import {
  dataPie,
  legendPie,
  dataSales,
  optionsSales,
  responsiveSales,
  legendSales,
  dataBar,
  optionsBar,
  responsiveBar,
  legendBar
} from "../../variables/Variables.jsx";
import Survey1 from "../../assets/img/survey1.png";
import { Link } from "react-router-dom";

class Dashboard extends Component {
  createLegend(json) {
    var legend = [];
    for (var i = 0; i < json["names"].length; i++) {
      var type = "fa fa-circle text-" + json["types"][i];
      legend.push(<i className={type} key={i} />);
      legend.push(" ");
      legend.push(json["names"][i]);
    }
    return legend;
  }
  render() {
    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <div className="row justify-content-center">
              <div className="col-md-3">
                <div className="card">
                  <div
                    className="card-header text-white"
                    style={{ backgroundColor: "#b7efeb", height: "80px" }}
                  >
                    <p className="text-center" style={{ paddingTop: "30px" }}>
                      Robustness
                    </p>
                  </div>
                  <div className="card-body">
                    <h4 className="card-title">Special title treatment</h4>
                    <p className="card-text">
                      With supporting text below as a natural lead-in to
                      additional content.
                    </p>

                    <Link to="/survey" className="btn btn-primary">
                      Go
                    </Link>
                  </div>
                  <div class="progress">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      aria-valuenow="70"
                      aria-valuemin="0"
                      aria-valuemax="100"
                      style={{ width: "60%" }}
                    >
                      60%
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-md-3">
                <div className="card">
                  <div
                    className="card-header text-white"
                    style={{ backgroundColor: "#b7efeb", height: "80px" }}
                  >
                    <p className="text-center" style={{ paddingTop: "30px" }}>
                      Redundancy
                    </p>
                  </div>
                  <div className="card-body">
                    <h4 className="card-title">Special title treatment</h4>
                    <p className="card-text">
                      With supporting text below as a natural lead-in to
                      additional content.
                    </p>
                    <Link to="/survey" className="btn btn-primary">
                      Go
                    </Link>
                  </div>
                  <div class="progress">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      aria-valuenow="70"
                      aria-valuemin="0"
                      aria-valuemax="100"
                      style={{ width: "70%" }}
                    >
                      70%
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-md-3">
                <div className="card">
                  <div
                    className="card-header text-white"
                    style={{ backgroundColor: "#b7efeb", height: "80px" }}
                  >
                    <p className="text-center" style={{ paddingTop: "30px" }}>
                      Resourcefulness
                    </p>
                  </div>
                  <div className="card-body">
                    <h4 className="card-title">Special title treatment</h4>
                    <p className="card-text">
                      With supporting text below as a natural lead-in to
                      additional content.
                    </p>
                    <Link to="/survey" className="btn btn-primary">
                      Go
                    </Link>
                  </div>
                  <div class="progress">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      aria-valuenow="70"
                      aria-valuemin="0"
                      aria-valuemax="100"
                      style={{ width: "80%" }}
                    >
                      80%
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-md-3">
                <div className="card">
                  <div
                    className="card-header text-white"
                    style={{ backgroundColor: "#b7efeb", height: "80px" }}
                  >
                    <p className="text-center" style={{ paddingTop: "30px" }}>
                      Rapidity
                    </p>
                  </div>
                  <div className="card-body">
                    <h4 className="card-title">Special title treatment</h4>
                    <p className="card-text">
                      With supporting text below as a natural lead-in to
                      additional content.
                    </p>
                    <Link to="/survey" className="btn btn-primary">
                      Go
                    </Link>
                  </div>
                  <div class="progress">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      aria-valuenow="70"
                      aria-valuemin="0"
                      aria-valuemax="100"
                      style={{ width: "100%" }}
                    >
                      100%
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </Row>
        </Grid>
      </div>
    );
  }
}

export default Dashboard;
