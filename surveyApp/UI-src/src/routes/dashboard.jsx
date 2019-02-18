import Dashboard from "../views/Dashboard/Dashboard";
import UserProfile from "../views/UserProfile/UserProfile";
import TableList from "../views/TableList/TableList";
import Typography from "../views/Typography/Typography";
import Icons from "../views/Icons/Icons";
import Maps from "../views/Maps/Maps";
import Notifications from "../views/Notifications/Notifications";
import SurveyUpload from "../views/Admin/surveyUpload";
import ReleseSurvey from "../views/Admin/releaseSurvey";
import UserUpload from "../views/Admin/userUpload";

const dashboardRoutes = [
  // {
  //   path: "/dashboard",
  //   name: "Resiliense",
  //   icon: "pe-7s-graph",
  //   component: Dashboard
  // },
  // {
  //   path: "/user",
  //   name: "User Profile",
  //   icon: "pe-7s-user",
  //   component: UserProfile
  // },
  // {
  //   path: "/survey",
  //   name: "Survey List",
  //   icon: "pe-7s-note2",
  //   component: SurveyList
  // }
  // {
  //   path: "/uservalidate",
  //   name: "Login Page",
  //   icon: "pe-7s-user",
  //   component: ValidateLogin,
  //   routes: [
  //     {
  //       path: "/uservalidate/registration",
  //       name: "Registration Page",
  //       icon: "pe-7s-user",
  //       component: UserRegistraion
  //     },
  //     {
  //       path: "/uservalidate/login",
  //       name: "Registration Page",
  //       icon: "pe-7s-user",
  //       component: Login
  //     },
  //     {
  //       path: "/uservalidate/survey",
  //       name: "Survey List",
  //       icon: "pe-7s-note2",
  //       component: SurveyList
  //     }
  //   ]
  // },

  {
    path: "/surveyupload",
    name: "Upload Survey",
    icon: "pe-7s-note2",
    component: SurveyUpload
  },
  {
    path: "/userdataupload",
    name: "Upload User Data",
    icon: "pe-7s-user",
    component: UserUpload
  },
  {
    path: "/releasesurvey",
    name: "Release Survey",
    icon: "pe-7s-note2",
    component: ReleseSurvey
  }

  // {
  //   path: "/typography",
  //   name: "Typography",
  //   icon: "pe-7s-news-paper",
  //   component: Typography
  // },
  // { path: "/icons", name: "Icons", icon: "pe-7s-science", component: Icons },
  // { path: "/maps", name: "Maps", icon: "pe-7s-map-marker", component: Maps },
  // {
  //   path: "/notifications",
  //   name: "Notifications",
  //   icon: "pe-7s-bell",
  //   component: Notifications
  // },
  // {
  //   upgrade: true,
  //   path: "/upgrade",
  //   name: "Upgrade to PRO",
  //   icon: "pe-7s-rocket",
  //   component: Upgrade
  // },
  // { redirect: true, path: "/", to: "/dashboard", name: "Dashboard" }
];

export default dashboardRoutes;
