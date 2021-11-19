from ..workers.models import Worker
from ..payTime.models import PayTime
from ..evaluation.models import MonthlyMeliaEvaluation
from ..evaluation.serializers.monthlyMeliaEvaluationSerliazer import MonthlyMeliaEvaluationMiniSerliazer


def getMeliaEvaluation(pay_time: PayTime, worker: Worker):
    if MonthlyMeliaEvaluation.objects.filter(payTime__id=pay_time.id,
                                             evaluateWorker__no_interno=worker.no_interno).exists():
        model = MonthlyMeliaEvaluation.objects.get(payTime__id=pay_time.id,
                                                   evaluateWorker__no_interno=worker.no_interno)
        return MonthlyMeliaEvaluationMiniSerliazer(model, many=False).data
    return None


def buildEval(length: int, index: int, paytimes: [], worker: Worker) -> MonthlyMeliaEvaluation or None:
    # Build  Eval
    evaluation = None
    if len(paytimes) >= length:
        paytime = paytimes[index]
        evaluation = getMeliaEvaluation(paytime, worker)
    return evaluation


def buildListItemOrder(newItem: {}, newTuple: [], key: str):
    if newItem[key] is not None:
        newTuple.append(newItem[key])
    else:
        newTuple.append(1000)
