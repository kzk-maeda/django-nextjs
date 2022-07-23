import Layout from "../../components/layout/layout";
import JobDetails from "../../components/job/JobDetails";

import axios from "axios";

export default function JobDetailsPage({ job, candidates }) {
  console.log(job, candidates);
  return (
    <Layout>
      <JobDetails job={job} candidates={candidates} />
    </Layout>
  );
}

export async function getServerSideProps({ params }) {
  const res = await axios.get(`${process.env.API_URL}/api/jobs/${params.id}/`);
  // console.log(res.data);
  const job = res.data.job;
  const candidates = res.data.candidates;

  return {
    props: {
      job,
      candidates,
    },
  };
}
