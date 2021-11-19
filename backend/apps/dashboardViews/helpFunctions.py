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


def selection_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k]['firstEvalTotal'] < collection[least]['firstEvalTotal']:
                least = k
        if least != i:
            collection[least], collection[i] = (collection[i], collection[least])
    