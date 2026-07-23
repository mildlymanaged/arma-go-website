export const siteName = "Arma Go";
export const siteDescription =
  "Work and study abroad guidance from the UAE.";

export const emails = {
  general: "hello@armago.me",
  partnerships: "partnerships@armago.me",
} as const;

export const mailto = {
  general: "mailto:hello@armago.me?subject=Arma%20Go%20Enquiry",
  work: "mailto:hello@armago.me?subject=Work%20Abroad%20Enquiry",
  study: "mailto:hello@armago.me?subject=Study%20Abroad%20Enquiry",
  partnerships:
    "mailto:partnerships@armago.me?subject=Employer%20or%20Partner%20Enquiry",
} as const;

export const navItems = [
  { label: "Home", href: "/" },
  { label: "Work Abroad", href: "/work-abroad" },
  { label: "Study Abroad", href: "/study-abroad" },
  { label: "Employers & Partners", href: "/employers-partners" },
  { label: "How It Works", href: "/how-it-works" },
  { label: "Resources", href: "/resources" },
  { label: "About", href: "/about" },
  { label: "Contact", href: "/contact" },
] as const;

export const sitePath = (path: string) => {
  if (
    path.startsWith("mailto:") ||
    path.startsWith("http://") ||
    path.startsWith("https://") ||
    path.startsWith("#")
  ) {
    return path;
  }
  const base = import.meta.env.BASE_URL.replace(/\/$/, "");
  const clean = path.startsWith("/") ? path : `/${path}`;
  const hasFileExtension = /\/[^/]+\.[a-z0-9]+$/i.test(clean);
  const normalized =
    clean === "/" || clean.endsWith("/") || hasFileExtension
      ? clean
      : `${clean}/`;
  return `${base}${normalized}` || "/";
};

export const pageMeta = {
  home: {
    title: "Work & Study Abroad Guidance UAE | Arma Go",
    description:
      "Explore work and study abroad options from the UAE. Understand requirements, prepare documents and applications, and plan your next steps with Arma Go.",
  },
  work: {
    title: "Work Abroad From the UAE | Arma Go",
    description:
      "Explore work abroad options from the UAE. Understand job requirements, documents, application stages, costs and preparation with Arma Go.",
  },
  study: {
    title: "Study Abroad From the UAE | Arma Go",
    description:
      "Explore study abroad options from the UAE. Compare programs, requirements, documents, budgets and application steps with Arma Go.",
  },
  partners: {
    title: "International Recruitment & Candidate Support UAE | Arma Go",
    description:
      "Arma Go supports employers and partners with international candidate sourcing, preparation, recruitment coordination and mobility support from the UAE.",
  },
  process: {
    title: "How Arma Go Works | Work & Study Support UAE",
    description:
      "See how Arma Go helps people understand work and study options, prepare documents, follow applications and plan their next steps from the UAE.",
  },
  resources: {
    title: "Work & Study Abroad Guides UAE | Arma Go Resources",
    description:
      "Read practical Arma Go guides about work abroad, study abroad, documents, requirements, applications, costs and international application preparation.",
  },
  about: {
    title: "About Arma Go | Work & Study Abroad Guidance UAE",
    description:
      "Learn how Arma Go helps people in the UAE understand work and study options, prepare important steps and make more informed decisions abroad.",
  },
  contact: {
    title: "Contact Arma Go UAE | Work, Study & Partnership Enquiries",
    description:
      "Contact Arma Go about work abroad, study abroad, documents, applications, employer partnerships and international guidance from the UAE.",
  },
  faq: {
    title: "Work & Study Abroad FAQs UAE | Arma Go",
    description:
      "Find answers about Arma Go, work and study abroad options, documents, eligibility, costs, timelines and employer partnerships.",
  },
  privacy: {
    title: "Privacy Policy | Arma Go",
    description:
      "Draft privacy policy for the Arma Go website, pending qualified legal review.",
  },
  terms: {
    title: "Terms and Conditions | Arma Go",
    description:
      "Draft terms and conditions for the Arma Go website, pending qualified legal review.",
  },
  refunds: {
    title: "Refund and Cancellation Policy | Arma Go",
    description:
      "Draft refund and cancellation policy for Arma Go, pending qualified legal review.",
  },
} as const;

export const imageAssets = {
  home: {
    src: "/images/home-guidance-v3.webp",
    width: 1572,
    height: 1001,
    alt: "A person walking through a dramatic forest-green architectural passage illuminated by warm directional light.",
  },
  work: {
    src: "/images/work-abroad-v2.webp",
    width: 1511,
    height: 941,
    alt: "A diverse group of professionals in hospitality, healthcare, childcare and business standing together against a warm neutral background.",
  },
  study: {
    src: "/images/study-abroad.webp",
    width: 1448,
    height: 1086,
    alt: "An adult learner researching at a laptop in a calm green and ivory study space.",
  },
  partners: {
    src: "/images/employers-partners.webp",
    width: 1793,
    height: 877,
    alt: "A diverse professional team in a natural discussion around a contemporary office table.",
  },
  process: {
    src: "/images/how-it-works.webp",
    width: 1800,
    height: 802,
    alt: "A sequence of connected architectural spaces linked by warm light and angular openings.",
  },
  about: {
    src: "/images/about-architecture.webp",
    width: 1733,
    height: 907,
    alt: "Contemporary ivory architecture with forest-green shadow planes, warm sunlight and blue sky.",
  },
  resources: {
    src: "/images/resources-still-life.webp",
    width: 1536,
    height: 1024,
    alt: "An organised ivory and green workspace with notebooks, a blank tablet and writing tools.",
  },
} as const;

export const featuredResources = [
  // Add each future article URL to href when the guide is published.
  {
    title:
      "Questions to Ask Before Paying for Work or Study Abroad Support",
    href: "",
  },
  { title: "Documents to Check Before Applying Abroad", href: "" },
  {
    title: "Work Abroad or Study Abroad: Which Route Fits Your Goal?",
    href: "",
  },
  { title: "How International Application Timelines Work", href: "" },
  {
    title: "What to Prepare for Your First Work or Study Consultation",
    href: "",
  },
] as const;

export const resourceArticles = [
  // Replace an empty href with the future article URL when content is ready.
  { title: "How to Evaluate a Work Abroad Opportunity From the UAE", href: "" },
  { title: "Documents to Check Before Applying for Work Abroad", href: "" },
  {
    title:
      "Questions to Ask Before Paying for Work or Study Abroad Support",
    href: "",
  },
  {
    title: "Work Abroad or Study Abroad: How to Compare the Two Routes",
    href: "",
  },
  {
    title: "What Can Affect an International Application Timeline?",
    href: "",
  },
  {
    title: "How to Prepare for a Work or Study Abroad Consultation",
    href: "",
  },
  {
    title: "What Does Eligibility Mean in a Work Abroad Application?",
    href: "",
  },
  {
    title: "How to Understand the Total Cost of Working or Studying Abroad",
    href: "",
  },
  {
    title: "Common Document Problems That Can Delay an Application",
    href: "",
  },
  {
    title: "Who Controls Each Stage of an International Application?",
    href: "",
  },
  { title: "What Happens After You Contact Arma Go?", href: "" },
  {
    title: "Seven Signs an Opportunity Abroad Needs More Explanation",
    href: "",
  },
  {
    title: "Why Candidate Readiness Matters in International Recruitment",
    href: "",
  },
  {
    title:
      "What Employers Should Clarify Before Recruiting International Candidates",
    href: "",
  },
] as const;

export const faqItems = [
  {
    question: "What does Arma Go do?",
    answer: [
      "Arma Go helps people in the UAE understand and prepare for work and study options abroad.",
      "Depending on the option and agreed service, support may include basic requirement checks, document preparation, application coordination, timelines, updates and guidance on next steps.",
      "Arma Go may also support employers and partners with candidate sourcing, readiness, recruitment coordination and mobility support.",
    ],
  },
  {
    question: "Does Arma Go guarantee jobs?",
    answer: [
      "No.",
      "Hiring decisions are made by employers and may depend on the applicant’s experience, qualifications, interviews, documents and other requirements.",
      "Arma Go may support the preparation and coordination included within the agreed service, but it does not guarantee employment.",
    ],
  },
  {
    question: "Does Arma Go guarantee visas or permits?",
    answer: [
      "No.",
      "Visa and permit decisions are made by the relevant authorities. Requirements, processing times and outcomes may vary.",
    ],
  },
  {
    question: "Does Arma Go guarantee admission to a school or university?",
    answer: [
      "No.",
      "Admission decisions are made by the relevant education provider and may depend on academic, language, financial and other requirements.",
    ],
  },
  {
    question: "Who can contact Arma Go?",
    answer: [
      "Arma Go primarily supports people in the UAE exploring work or study options abroad.",
      "Employers and partners seeking international candidate, recruitment or mobility support may also contact the team.",
    ],
  },
  {
    question: "What email should I use for work or study enquiries?",
    answer: [
      "Email hello@armago.me.",
      "Include a short explanation of your current situation, what you are exploring and the questions you would like answered.",
    ],
  },
  {
    question: "What email should I use for employer or partner enquiries?",
    answer: [
      "Email partnerships@armago.me.",
      "Include your organisation name, location, the type of partnership or support required and your preferred timeline.",
    ],
  },
  {
    question: "What should I include in my first email?",
    answer: [
      "For work or study enquiries, include:",
      "• Your full name\n• Your current location\n• Whether you are exploring work or study\n• Your current occupation or education\n• Your preferred destination, if known\n• Your preferred timeline\n• Your main questions",
      "For employer or partner enquiries, include:",
      "• Your organisation name\n• Your location\n• The type of service or partnership required\n• The roles, candidates or project involved\n• Your preferred timeline\n• Your contact details",
    ],
  },
  {
    question: "Do I need to send my passport with my first enquiry?",
    answer: [
      "No.",
      "Do not send passports, identification documents or sensitive personal information in your first email.",
      "The Arma Go team will let you know if documents are required later and how they should be provided.",
    ],
  },
  {
    question: "Can Arma Go tell me whether I qualify?",
    answer: [
      "Arma Go may review basic requirements based on the information available.",
      "Final eligibility or approval may depend on complete supporting information and decisions made by employers, institutions or authorities.",
    ],
  },
  {
    question: "Can Arma Go help with documents?",
    answer: [
      "Depending on the option and agreed service, Arma Go may help identify required documents, organise the checklist and support preparation for the applicable stage.",
      "Document requirements differ by destination and application type.",
    ],
  },
  {
    question: "How long does the process take?",
    answer: [
      "Timelines vary according to the option, destination, applicant, document readiness and decisions made by third parties.",
      "Arma Go will explain the known stages and timing variables for the option being discussed.",
    ],
  },
  {
    question: "How much does the service cost?",
    answer: [
      "Fees depend on the option and agreed service scope.",
      "Before proceeding, you should receive information explaining:",
      "• What services are included\n• What services are excluded\n• When payments are due\n• Which costs are paid to third parties\n• Any applicable refund or cancellation conditions",
    ],
  },
  {
    question: "Can I contact Arma Go if I do not know which country to choose?",
    answer: [
      "Yes.",
      "You can begin by explaining your goal, background, budget and preferred timeline.",
      "Arma Go can then discuss the types of options that may be worth exploring.",
    ],
  },
] as const;
