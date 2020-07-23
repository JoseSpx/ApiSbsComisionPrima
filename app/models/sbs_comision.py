class SbsComision:
    def __init__(self, afp='', comision_fija='', comision_sobre_flujo='', comision_mixta_csf='', comision_mixta_cas='',
                 prima_seguros='', aporte_obligatorio='', remuneracion_maxima=''):
        self.afp = afp
        self.comision_fija = comision_fija
        self.comision_sobre_flujo = comision_sobre_flujo
        self.comision_mixta_csf = comision_mixta_csf
        self.comision_mixta_cas = comision_mixta_cas
        self.prima_seguros = prima_seguros
        self.aporte_obligatorio = aporte_obligatorio
        self.remuneracion_maxima = remuneracion_maxima

    def serialize(self):
        return {
            'afp': self.afp,
            'comision_fija': self.comision_fija,
            'comision_sobre_flujo': self.comision_sobre_flujo,
            'comision_mixta_csf': self.comision_mixta_csf,
            'comision_mixta_cas': self.comision_mixta_cas,
            'prima_seguros': self.prima_seguros,
            'aporte_obligatorio': self.aporte_obligatorio,
            'remuneracion_maxima': self.remuneracion_maxima
        }
