import http from "./httpService";

// const apiEndpoint = apiUrl + "/movies";

export function surveyUpload(Survey_name, company_name) {
  const url = `http://127.0.0.1:5000/questionsUpload?survey=${Survey_name}&company=${company_name}`;
  return http.post(url, { Survey_name, company_name });
}
export function userdataupload(Survey_name, company_name) {
  const url = `http://127.0.0.1:5000/usersUpload?survey=${Survey_name}&company=${company_name}`;
  return http.post(url, { Survey_name, company_name });
}
