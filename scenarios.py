"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""
"""Unit 8 - Milestone 3: Acceptance criteria evaluation.

Criteria 1, 2, and 5 run through /submit.
Criteria 3 and 4 require separate tests because the original
run_eval.py only sends requests to /submit.
"""

SCENARIOS = [
    {
        "name": "False Positive Protection",
        "criterion": 1,
        "texts": [
            # H01
            """When I was a teenager, I learned programming. That was a long time ago, and the language I learned is no longer used, but the principles are still with me, and they gave me a problem-solving mindset. This shows that languages change, but the way of thinking stays.  That is why I believe the best age to teach programming is between 10 and 12 years old. I mean, introducing programming at that age would be great because at that age kids can think logically and build problem-solving, analytical, and critical thinking skills using simple tools; those skills they will carry to any career.""",

            # H02
            """In a business environment like BrightPay Solutions, comments are important because usually the programs are developed and maintained by different people. For example, they now want to automate employee tax calculation. That program is running well, but without comments, future updates or improvements could be more difficult. The development team might change over time, and new developers may not understand certain parts of the code or may need more time to figure out how to implement an update.""",

            # H03
            """Yesterday, I went to the doctor for my anual physical evaluation. I believe prevention is very important, so each year I schedule my anual physical appoinments carefully.  When you are younger, usually heath issues do not matter, but when you are over the forties you need to take care of your health more.""",

            # H04
            """My background is a mix of business, operations, and compliance.  I have over 15 years of experience in the banking sector, working in areas such as operations, risk management, compliance, and process improvement.  After COVID, as everything became more digital, I decided to move into cybersecurity. To build the foundations,  I got an Associate Degree in Cybersecurity and obtained a Security+ certification.""",

            # H05
            """The design uses private IPv4 addressing and VLSM to give each VLAN a subnet size based on the estimated number of devices that need to connect to it. The connection between the campus and the Internet will be provided by a Firewall/router, and a Layer 3 switch will support communication between VLANs.  Managed access switches will provide wired connectivity, and wireless access points will provide separate wireless networks for employees, students, and guests.""",

            # H06
            """Huayruro is the name a seed from the rainforest of Peru. People who live in the Peruvian Amazon belives Huaruro is a Lucky Seed, so when a baby is born they give them a brazalet with a small huayruro as a symbol of protection and good luck""",

            # H07
            """When you are designing a network, many things come into play: the client's needs, priorities, and goals. In my case, I wanted to propose a network design that meets Trine University requirements and prioritizes security over budget. As I worked on the design, I discovered some things that made me go back and review my original proposal.  In my case, I decided in Phase 2 to go over the assumptions again to make them more realistic.""",

            # H08
            """In my opinion, the two most important devices in the proposed network design are the firewall and the Layer 3 core switch. The firewall is the entry point of Trine University’s network, so it needs to handle campus network traffic efficiently, control incoming and outgoing traffic, and help protect the Trine University network from external threats. Since the firewall protects the network’s internet connection, the Layer 3 core switch will handle routing between each VLAN.""",

            # H09
            """My daughter is a rising 8th grader and very interested in participating in LiT, so I wanted to ask whether there may still be opportunities available at Springwoods and whether scholarship support may be available for the program.

She currently serves as a teacher assistant at her ballet academy (SBDCRC School of Dance), helping younger students, and she really enjoys leadership opportunities and working with children.""",

            # H10
            """My favorite book is The Little Prince. My father used to read that book to me every night when I was a kid. I dreamed of one day having the luck to know the planets the Little Prince had traveled to. Later, when I was a teenager, I read it again and found different parts of the book, especially the relationship between the Little Prince and the fox.  In the following years, I read it again and  understood how deep a friendship could be. """,
        ],
    },

    {
        "name": "AI-Generated Text Detection",
        "criterion": 2,
        "texts": [
            # A01
            """Effective project management requires a structured approach to planning, execution, and evaluation. Organizations should define measurable objectives, assign responsibilities, and establish communication channels. Regular progress reviews enable teams to identify emerging risks, adjust priorities, and maintain alignment with strategic goals. By combining clear documentation with continuous feedback, businesses can improve accountability, reduce delays, and deliver more consistent outcomes across departments.""",

            # A02
            """Cybersecurity awareness is an essential component of organizational resilience. Employees should understand common phishing techniques, password security principles, and the importance of reporting suspicious activity. Training programs are most effective when they use practical examples and periodic reinforcement. In addition, leadership support helps establish a culture in which protecting information is considered a shared responsibility rather than solely a technical function.""",

            # A03
            """Urban green spaces provide environmental, social, and public health benefits. Trees can reduce local temperatures, support biodiversity, and improve air quality. Parks also offer opportunities for exercise and community interaction. City planners should consider accessibility, maintenance costs, and long-term ecological outcomes when developing green infrastructure. A balanced approach can help communities adapt to climate pressures while improving residents' quality of life.""",

            # A04
            """A well-designed customer service process balances efficiency with empathy. Businesses can use automated systems to answer routine questions, while reserving complex situations for trained employees. Clear escalation procedures reduce confusion and help customers receive timely support. Organizations should monitor response times and customer feedback, but they should also evaluate whether their processes resolve underlying problems rather than simply closing tickets quickly.""",

            # A05
            """Renewable energy adoption involves several interconnected considerations. Solar and wind technologies can reduce reliance on fossil fuels, but their output varies with environmental conditions. Energy storage, grid modernization, and demand management can help address this variability. Policymakers must also consider affordability, land use, and supply-chain constraints. A diversified energy strategy can support reliability while advancing long-term sustainability goals.""",

            # A06
            """Learning a second language offers benefits that extend beyond vocabulary acquisition. Students develop communication strategies, cultural awareness, and greater sensitivity to context. Consistent practice is often more effective than occasional intensive study. Listening, reading, speaking, and writing reinforce one another, especially when learners receive constructive feedback. A supportive environment encourages experimentation and helps students become more confident communicators.""",

            # A07
            """Small businesses can benefit from adopting basic data analytics practices. Tracking sales trends, inventory turnover, and customer preferences can reveal opportunities for improvement. However, collecting more information does not automatically lead to better decisions. Owners need clear questions, reliable data, and straightforward visualizations. Even simple monthly reports can support planning when their findings are reviewed and translated into concrete actions.""",

            # A08
            """Healthcare organizations rely on accurate information exchange to coordinate patient care. Standardized records can improve continuity across departments, but implementation requires attention to privacy, staff training, and system compatibility. Clear access controls help protect sensitive information, while audit trails support accountability. Technology should be evaluated not only by its technical capabilities but also by how effectively it supports clinical workflows and patient safety.""",

            # A09
            """Educational technology can expand access to learning resources when it is implemented thoughtfully. Digital platforms allow students to revisit lessons, collaborate remotely, and receive timely feedback. Nevertheless, differences in connectivity and digital literacy may create barriers. Schools should provide accessible materials and alternative participation options. Successful integration depends on instructional goals, teacher preparation, and ongoing assessment of student outcomes.""",

            # A10
            """Supply chain resilience requires organizations to anticipate disruptions and prepare practical responses. Diversifying suppliers may reduce dependency on a single source, while inventory monitoring can identify emerging shortages. Companies should map critical dependencies and establish communication procedures for unexpected events. Periodic scenario exercises help teams test assumptions and improve coordination. These measures can strengthen continuity without eliminating every operational risk.""",
        ],
    },

    {
        "name": "API Input Validation",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_invalid_01"},
            {"creator_id": "eval_invalid_02"},
            {"text": None, "creator_id": "eval_invalid_03"},
            {"text": 123, "creator_id": "eval_invalid_04"},
            {"text": True, "creator_id": "eval_invalid_05"},
            {"text": [], "creator_id": "eval_invalid_06"},
            {"text": {}, "creator_id": "eval_invalid_07"},
            {"text": "   ", "creator_id": "eval_invalid_08"},
            {"text": "A normal text without creator ID."},
            {"text": "word " * 50000, "creator_id": "eval_invalid_10"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
