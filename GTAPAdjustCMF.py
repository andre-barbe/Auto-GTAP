__author__ = "Andre Barbe"
__project__ = "Auto-GTAP"
__created__ = "2018-5-4"
__altered__ = "2018-5-4"

from SimulationShocks import SimulationShocks


class GTAPAdjustCMF(object):
    """Creates an CMF file for controlling gemsim when it runs the GTAP adjust (as opposed to the policy simulation)"""

    __slots__ = ["simulation_name", "solution_method", "model_folder", "shock_type"]

    def __init__(self, simulation_name: str, solution_method: str, model_folder: str, shock_type: str) -> None:
        self.solution_method = solution_method
        self.model_folder = model_folder
        self.shock_type = shock_type
        self.simulation_name = simulation_name

        cmf_file_name = "gtapadjust.cmf"

        line_list_main = [
            'auxiliary files = GtapAdjust;\n',
            '!check-on-read elements = warn; ! Optional: very often needed\n',
            'cpu=yes ; ! Optional: Reports CPU times for various stages\n',
            'log file = GtapAdjust.log;  ! Optional\n',
            '! Input files:\n',
            'File INFILE = work\orig.har; ! Normalized GTAP data - containing flows and sets\n',
            '! Output files:\n',
            'File Initial = work\InitialRpt.har; ! Diagnostic output for pre-adjustment data\n',
            'File Final   = work\FinalRpt.har;   ! Diagnostic output for post-adjustment data\n',
            'Solution File = work\\adjust;        ! Diagnostic output \n',
            '! Updated files:\n',
            'Updated File INFILE = work\\adjusted.har; ! Adjusted Normalized GTAP data \n',
            '\n',
            '! Solution method\n',
            'method = Euler ;\n',
            'steps = 6;\n',
            'start with mmnz = 2000000;\n',
            '\n',
            '! Automatic closure generated by TABmate Tools...Closure command\n',
            '!              Variable     Size \n',
            'Exogenous      domslack ; ! IND*REG   slack to scale all flows entering into COSTS so that COSTS=SALES\n',
            'Exogenous      impslack ; ! COM*REG   Slack to scale TRADE to balance Regional imports\n',
            'Exogenous      marslack ; ! MAR   Slack to scale VST to balance supply/demand of shipping margins\n',
            'Exogenous      q1absorp ; ! FIN*REG   GDP/absorption link variable\n',
            'Exogenous      q3absorp ; ! 1   World GDP/absorption link variable\n',
            'Exogenous          qdem ; ! COM*REG   scales ALL use of c made in f\n',
            'Exogenous          qexp ; ! COM*REG   Export factor: use to target exports\n',
            'Exogenous       qexpend ; ! FIN*REG   Absorption factors: to target C, I, G\n',
            '!Exogenous        qtrdbi ; ! COM*REG*REG   scales exports from f to t [to target vTRADE_FOB]\n',
            'Exogenous       qexptot ; ! REG   Export factor: use to target aggregate exports\n',
            'Exogenous          qfac ; ! FAC*REG   to target [parts of] vGDPFACS(f,r)\n',
            'Exogenous          qimp ; ! COM*REG   Import factor: use to target imports\n',
            'Exogenous       qimptot ; ! REG   Import factor: use to target aggregate imports\n',
            'Exogenous       qnatsiz ; ! REG   Size factor: use to target national GDP\n',
            'Exogenous       qNATTAX ; ! COM*REG   to target NATTAX\n',
            'Exogenous    qNATTAXTOT ; ! REG   to target NATTAXTOT\n',
            'Exogenous       qTRDTAX ; ! COM*TRD*REG   to target TRDTAX\n',
            'Exogenous    qTRDTAXTOT ; ! TRD*REG   to target TRDTAXTOT\n',
            'Rest endogenous; ! end of TABmate automatic closure\n',
            '\n',
            '!    old exog      new exog   !   \n',
            'swap  domslack = dDOMCHECK;  ! scale industry costs to force costs=sales\n',
            'swap  impslack = dIMPCHECK;  ! scale trade matrix to force supply=demand for imports\n',
            'swap  marslack = dMARCHECK;  ! scale VST matrix to force supply=demand for shipping\n',
            '\n',
            '! remove pre-existing imbalances !\n',
            'final_level  dDOMCHECK = uniform 0;   ! force costs=sales\n',
            'final_level  dIMPCHECK = uniform 0;   ! force supply=demand for imports\n',
            'final_level  dMARCHECK = uniform 0;   ! force supply=demand for shipping\n',
            '\n',
            '! Optional link to make absorption follow GDP: use with caution (see TAB)\n',
            '!    old exog      new exog   !   \n',
            '!swap  q1absorp = q2absorp;  ! optional: link aborption to GDP \n',
            '!swap  q3absorp = vGDPWLD;   ! needed if q2absorb exogenous; fix world GDP  \n',
            '\n',
            '!********** YOU SHOULD NORMALLY EDIT ONLY BELOW THIS LINE ***********! \n'
        ]

        line_list_shocks_original = [
            '\n',
            '!    old exog                new exog   !   \n',
            'swap qdem("omn","Australia")=vCOSTS("omn","Australia");\n',
            'final_level  vCOSTS("omn","Australia")= 50000; \n',
            '\n',
            '!    old exog      new exog   !   \n',
            '!swap qEXP("foodfrsfsh","Australia")=vEXPDEM("foodfrsfsh","Australia");\n',
            '!final_level  vEXPDEM("foodfrsfsh","Australia") = 40000;  \n',
            '\n',
            '!    old exog      new exog   !   \n',
            '!swap qimp("foodfrsfsh","Australia")=vIMPCIF("foodfrsfsh","Australia");\n',
            '!final_level  vIMPCIF("foodfrsfsh","Australia") = 10000;  \n',
            '\n',
            '!    old exog      new exog   !   \n',
            '!swap qexptot("Australia")=vGDPEXPS("Exp","Australia");\n',
            '!final_level  vGDPEXPS("Exp","Australia") = 170000;  \n',
            '\n',
            '!    old exog      new exog   !   \n',
            '!swap qtrdtax("omn","exp","Australia")=vTRDTAX("omn","exp","Australia");\n',
            '!final_level  vTRDTAX("omn","exp","Australia")= 12; \n',
            ' \n',
            '!    old exog      new exog   !   \n',
            '!swap qtrdtax("foodfrsfsh","imp","Australia")=vTRDTAX("foodfrsfsh","imp","Australia");\n',
            '!final_level  vTRDTAX("foodfrsfsh","imp","Australia")= 200;  \n',
            '\n',
            '!    old exog      new exog   !   \n',
            '!swap qnattaxtot("Australia")=vNATTAXTOT("Australia");\n',
            '!final_level  vNATTAXTOT("Australia")= 50000;  \n',
            '\n',
            'Verbal Description = Adjust GTAP database  ;\n'
        ]

        line_list_shocks = [
            '\n',
            '!    old exog                new exog   !   \n',
            'swap qdem("GrainsCropsA","Oceania")=vCOSTS("GrainsCropsA","Oceania");\n',
            'final_level  vCOSTS("GrainsCropsA","Oceania")= 50000; \n',
            'Verbal Description = Adjust GTAP database  ;\n'
        ]

        # Combine line lists
        line_list_total = line_list_main + line_list_shocks

        # Create final file
        cmf_file_name_with_path = "Work_Files\\" + self.simulation_name + "\\" + self.model_folder + "\\input\\" + cmf_file_name
        with open(cmf_file_name_with_path, "w+") as writer:  # Create the empty file
            writer.writelines(line_list_total)  # write the line list to the file
