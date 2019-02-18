import Dashboard from "../layouts/Dashboard/Dashboard.jsx";
import UserProfile from "../components/userComponent/loginForm";
import ValidateLogin from "../components/userComponent/loginForm";

var indexRoutes = [
  { path: "/", name: "Home", component: Dashboard },
  { path: "/logintest", name: "logintest", component: ValidateLogin }
];

export default indexRoutes;
