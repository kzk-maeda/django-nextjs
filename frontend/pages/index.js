import Layout from "../components/layout/layout";
import Home from "../components/Home";

import axios from "axios";

export default function Index({ data }) {
  // console.log("jobs", data);
  return (
    <Layout>
      <Home data={data} />
    </Layout>
  );
}

export async function getServerSideProps({ query }) {
  const keyword = query.keyword || "";
  const location = query.location || "";
  const jobType = query.jobType || "";
  const education = query.education || "";
  const experience = query.experience || "";

  let min_salary = "";
  let max_salary = "";

  if (query.salary) {
    const [min, max] = query.salary.split("-");
    min_salary = min;
    max_salary = max;
  }

  const page = query.page || 1;

  const queryString = `keyword=${keyword}&location=${location}&page=${page}&jobType=${jobType}&education=${education}&experience=${experience}&min_salary=${min_salary}&max_salary=${max_salary}`;
  // console.log(query);

  const res = await axios.get(`${process.env.API_URL}/api/jobs?${queryString}`);
  const data = res.data;

  return {
    props: {
      data,
    },
  };
}
