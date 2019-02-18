import React from "react";
import ReactDOM from "react-dom";

import { HashRouter, Route, Switch } from "react-router-dom";

import indexRoutes from "./routes/index";

import "bootstrap/dist/css/bootstrap.min.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "startbootstrap-sb-admin/css/sb-admin.css";
import "./assets/css/animate.min.css";
import "./assets/sass/light-bootstrap-dashboard.css?v=1.2.0";
import "./assets/css/demo.css";
import "./assets/css/pe-icon-7-stroke.css";

import AdminLogin from "./views/Admin/adminLogin";

ReactDOM.render(
  <HashRouter>
    <Switch>
      {/* {indexRoutes.map((prop, key) => {
        return <Route to={prop.path} component={prop.component} key={key} />;
      })} */}

      <Route path="/adminlogin" component={AdminLogin} />

      {indexRoutes.map((prop, key) => {
        return <Route to={prop.path} component={prop.component} key={key} />;
      })}
      {/* <Route path="/products/:id" component={ProductDetails} />
      <Route
        path="/products"
        render={props => <Products sortBy="newest" {...props} />}
      />
      <Route path="/posts/:year?/:month?" component={Posts} />
      <Route path="/admin" component={Dashboard} />
      <Route path="/" component={Home} /> */}
    </Switch>
  </HashRouter>,
  document.getElementById("root")
);
