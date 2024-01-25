function init() {
    document.IQtest.Result.value="Test in progress...";
}

function myEval(str) {
    try {
	return eval(str);
    } catch(err) {
	return str.toUpperCase();
    }
}

function valTest() {
    sc=0;

    if (document.IQtest.q1.value.toUpperCase()=="M") {sc++;}
    if (document.IQtest.q2.value && myEval(document.IQtest.q2.value)==15){sc++;}
    if (document.IQtest.q3.value && myEval(document.IQtest.q3.value)==8) {sc++;}
    if (document.IQtest.q4.value && myEval(document.IQtest.q4.value)==6) {sc++;}
    if (document.IQtest.q5.value && myEval(document.IQtest.q5.value)==5) {sc++;}
    if (document.IQtest.q6.value && myEval(document.IQtest.q6.value)==4) {sc++;}
    if (document.IQtest.q7.value && myEval(document.IQtest.q7.value)==1) {sc++;}
    if (document.IQtest.q8.value && myEval(document.IQtest.q8.value)==2) {sc++;}

    if (document.IQtest.q9[2].checked==true) {sc++;}
    if (document.IQtest.q10[1].checked==true) {sc++;}
    if (document.IQtest.q11[2].checked==true) {sc++;}
    if (document.IQtest.q12[3].checked==true) {sc++;}
    if (document.IQtest.q13[3].checked==true) {sc++;}
    if (document.IQtest.q14[2].checked==true) {sc++;}
    if (document.IQtest.q15[2].checked==true) {sc++;}
    if (document.IQtest.q16[3].checked==true) {sc++;}
    if (document.IQtest.q17[1].checked==true) {sc++;}
    if (document.IQtest.q18[0].checked==true) {sc++;}

    if (document.IQtest.q19[0].checked==true &
	document.IQtest.q19[1].checked==false &
	document.IQtest.q19[2].checked==false &
	document.IQtest.q19[3].checked==true &
	document.IQtest.q19[4].checked==false) {sc++;}
    if (document.IQtest.q20[0].checked==false &
	document.IQtest.q20[1].checked==true &
	document.IQtest.q20[2].checked==true &
	document.IQtest.q20[3].checked==false &
	document.IQtest.q20[4].checked==false) {sc++;}
    if (document.IQtest.q21[0].checked==true &
	document.IQtest.q21[1].checked==false &
	document.IQtest.q21[2].checked==false &
	document.IQtest.q21[3].checked==true &
	document.IQtest.q21[4].checked==false) {sc++;}
    if (document.IQtest.q22[0].checked==false &
	document.IQtest.q22[1].checked==true &
	document.IQtest.q22[2].checked==false &
	document.IQtest.q22[3].checked==true &
	document.IQtest.q22[4].checked==false) {sc++;}

    if (document.IQtest.q23[3].checked==true) {sc++;}
    if (document.IQtest.q24[2].checked==true) {sc++;}
    if (document.IQtest.q25[1].checked==true) {sc++;}
    if (document.IQtest.q26[2].checked==true) {sc++;}

    if (document.IQtest.q27[1].checked==true) {sc++;}
    if (document.IQtest.q28[3].checked==true) {sc++;}
    if (document.IQtest.q29[2].checked==true) {sc++;}
    if (document.IQtest.q30[0].checked==true) {sc++;}
    if (document.IQtest.q31[2].checked==true) {sc++;}
    if (document.IQtest.q32[0].checked==true) {sc++;}
    if (document.IQtest.q32[3].checked==true) {sc++;}
    if (document.IQtest.q33[2].checked==true) {sc++;}

    document.IQtest.Result.value=fmtRes(sc);
}
